import os
import subprocess
import glob

'''
Egan, Henry, Teeron, Jonah, Andromeda Shell
'''

# Colored text
class Color:
	BAD = '\033[91m'	# Warnings, exceptions, etc. (red)
	IN = '\u001b[37m'	# User input and files (white)
	OUT = '\u001b[32m'	# Shell output (green)
	PROMPT = '\033[96m'	# Shell prompt (cyan)
	BOLD = '\u001b[35m'	# Bold (magenta)

# Changes working directory TODO: add shortcuts 
def cd(path):
	if path == "home":
		home = os.path.expanduser('~')	# Universal home directory
		os.chdir(home)
	else:
		try:
			os.chdir(path)
		except OSError:
			print(Color.BAD + "Unable to change current working directory")

# Turns input into list of tokens
def tokenize(inp):
	if inp[-1] != " ":	# Caters to appending commands based on spaces
		inp += " "

	cmd = ""
	quotes = False
	backslash = False
	tokens = []

	# Adds characters to command until space, unless quotes are around input. 
	# Backslashes stop fn of following char, currently only supports quotes. TODO wild cards
	for i in range(len(inp)):
		current = inp[i]
		if current == "\\":
			if not backslash:
				backslash = True
			else:
				backslash = False
		if current == '"':
			if not backslash:
				if not quotes:
					quotes = True
				else:
					quotes = False
			else:
				cmd += current
				backslash = False
		if current == " ":
			if not quotes:
				tokens.append(cmd)
				cmd = ""
			else:
				cmd += current
		elif current != '"' and not backslash:
			cmd += current

	return tokens

# Parses and executes tokens. Does not support semicolons.
# TODO $(x)
def parse(tokens):
	special_operators = [">", "<", "|", "&", "!"]
	expecting = "command"	# Shell always begins by expecting command
	arg_list = []

	waiting_op = False
	prev_proc = 0
	current_proc = 1
	proc_list = []

	has_operators = False

	# print(tokens)
	for i in range(len(tokens)):
		element = tokens[i]
		# TODO other special cases
		if expecting == "command":	# Command parsing segment
			if element == "echo":	# Echo special case
				new = ""
				for j in range(i + 1, len(tokens)):
					new += tokens[j] + " "
				print(new)
				break
			if element == "cd":	# Change CWD special case
				if len(tokens) == 1:
					cd("home")
				else:
					cd(tokens[i + 1])
				break
			else:
				# Check relevant cmd locations 	
				xok_bin = os.access("/bin/" + element, os.X_OK)
				xok_usrbin = os.access("/usr/bin/" + element, os.X_OK)
				xok_cwd = os.access(os.getcwd() + element, os.X_OK)
				xok_homedir = os.access(os.path.expanduser('~') + element, os.X_OK)

				if xok_bin or xok_usrbin or xok_cwd or xok_homedir:	# Check if executable 
					if len(tokens) == 1:
						subprocess.run(tokens)	# Execute tokens if only one command
					else:	# Appends full path just in case
						if xok_bin:
							arg_list.append("/bin/" + element)
						elif xok_usrbin:
							arg_list.append("/usr/bin/" + element)
						elif xok_cwd:
							arg_list.append(os.getcwd() + element)
						else:
							arg_list.append(os.path.expanduser('~') + element)
						expecting = "argument"
				else:
					print(Color.BAD + "Command not found. Type \"help\" for help.")
					break	# Stops if first command bad

		elif expecting == "argument":	# Parses other arguments, including wildcards
			# Wildcard expansion
			if "*" in element:
				for name in glob.glob(element):
					arg_list.append(name)
			if "?" in element:
				for name in glob.glob(element):
					arg_list.append(name)
			if "[" and "]" in element:
				for name in glob.glob(element):
					arg_list.append(name)
			else:
				arg_list.append(element)
			if i != len(tokens) - 1:	# Checks for upcoming operators
				next_token = tokens[i + 1]
				if next_token in special_operators:
					expecting = "operator"

		elif expecting == "operator": 
			proc_list.append(arg_list)
			has_operators = True
		
			arg_list = []
			if waiting_op:
				operate(element, proc_list[prev_proc], proc_list[current_proc])
				prev_proc += 1
				current_proc += 1
				waiting_op = False
			else:
				waiting_op = True

			expecting = "command"

		if i == len(tokens) - 1 and has_operators:	# Tail of operators
			proc_list.append(arg_list)
			operate(element, proc_list[prev_proc], proc_list[current_proc])

	if not has_operators:	# Shortcut
		try:
			subprocess.run(arg_list)
		except Exception:
			print(Color.BAD + "Error")


'''
			op_count += 1
			job_list.append(arg_list)
			arg_list = []

			if element == "|":
			# redirect stdout to one end of pipe
			# fork off code, it's filling up pipe in bg
			# when pipe is full it blocks process until it can be read
			# process next command direct stdin to ouput of previous pipe
				
				
			elif element == ">":
				pass
			elif element == "<":
				pass

			expecting = "command"
		
		# if no operators. 
		# using subprocess. keep global var of previous process and current process (between operator)
		# then, depending on operator, perform fn between processes. keep track of current, which becomes prev and so on
		# until end is reached

		# also keep list of jobs
		'''

# Directs input and output
def operate(operator, prev_proc, current_proc):
	out = None
	if operator == "|":
		proc1 = subprocess.Popen(prev_proc, stdout=subprocess.PIPE)
		proc2 = subprocess.Popen(current_proc, stdin=proc1.stdout, stdout=subprocess.PIPE)
		out = proc2.communicate()[0]

	elif operator == ">":
		pass
	elif operator == "<":
		pass
	print(out)
	return out	


# Returns number of operators in tokens
def get_operator_num(tokens, special_operators):
	n = 0
	for element in tokens:
		for op in special_operators:
			if element == op:
				n += 1
	return n


# Indicate superuser
def prompt():
	if os.geteuid() == 0:
		prompt = "# "
	else:
		prompt = "$ "
	return prompt

# Main
def main():
	print(Color.BOLD + "Welcome to ehtjash, a shell written in Python")
	while True:
		commands = input(Color.PROMPT + "ehtjash:" + str(os.path.basename(os.getcwd())) + " " + os.getlogin() + prompt() + Color.IN)
		if commands == "exit":
			print(Color.OUT + "Terminated")
			break
		elif commands == "help":
			help()
		else:
			tokens = tokenize(commands)
			parse(tokens)

if __name__ == "__main__":
	main()


# Old code
'''
import subprocess, os, glob
#import argparse

def main():
	while True: 
		command = input(ehtjash_pwd() + ":\033[1;32m $ \033[1;37m")
		if command == "exit":
			break
		elif command == "--help":
			prnt_help()
		elif "|" in command:
			command_list = command.split("|")
			output = pipe_center(command_list, None)
			if output is not None:
				print(output)
		else:
			command_list = command.split(" ")
			output = single_commands(command_list)
			if output is not None:
				print(output)


def pipe_center(command_list, stIn):
	command = command_list[0].split(" ")
	while "" in command:
		command.remove("")
	if len(command_list) > 1:
		try:
			p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=stIn)
			return pipe_center(command_list[1:], p.stdout)
		except FileNotFoundError:
			print("Command Not Found (。_。)")
	else:
		try:
			p = subprocess.Popen(command, stdout=subprocess.PIPE, 
				stdin=stIn)
			return getPopenOutput(p)
		except FileNotFoundError:
			print("Command Not Found (。_。)")


	parser = argparse.ArgumentParser()
	parser.add_argument("--help", dest = "help", type =str, action = "print_help")

	args = parser.parse_args()
	if (args == "--help"):
		print(prnt_help())

def getPopenOutput(process):
	output = str(process.communicate()[0])
	return output[2:len(output)-1].replace("\\n", "\n")
	
def single_commands(command_list):
	if command_list[0] == "pwd" or command_list[0] == "cwd":
		return ehtjash_pwd()
	elif command_list[0] == "cd":
		ehtjash_cd(command_list[1])
	else:
		try:
			p = subprocess.Popen(command_list, stdout=subprocess.PIPE)
			return getPopenOutput(p)
		except FileNotFoundError:
			print("Command Not Found (。_。)")

def ehtjash_cd(location):
	
	try:
		if location == "":
			os.chdir("/Users/" + os.getlogin())
		else:
			os.chdir(location)
	except:
		print("ehthash cd: no file or directory found")

def ehtjash_pwd():
	return str(os.getcwd())

#Put commands + descriptions 
def prnt_help():
	print("help segment")

if __name__ == "__main__":
	main()

'''