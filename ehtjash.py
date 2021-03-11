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

'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--help", dest = "help", type =str, action = "print_help")

	args = parser.parse_args()
	if (args == "--help"):
		print(prnt_help())
'''
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