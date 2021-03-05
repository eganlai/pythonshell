import subprocess
import os
import os.path
import sys
import argparse

def main():

	while True: 
		command = input(ehtjash_pwd() + ": $ ") #we use input here in the main() for simple commands
		if command == "exit":
			break
		elif command == "--help":
			prnt_help()
		else:
			command_list = command.split("|")
		command_center(command_list)

def command_center(command_list, stin):

	command_list

	if command_list.length() > 1:


		if command_list[i][0] == "pwd" or command_list[0] == "cwd":
			ehtjash_pwd()
		elif command_list[i][0] == "cd":
			ehtjash_cd(command_list[i][1])
		else:
			subprocess.Popen(command_list)
	else:
		# no stin 



	for i in command_list:
		i.split(" ")

	for i in command_list:

		if command_list[i][0] == "pwd" or command_list[0] == "cwd":
			ehtjash_pwd()
		elif command_list[i][0] == "cd":
			ehtjash_cd(command_list[i][1])
		elif pipeTest


		else:
			subprocess.Popen(command_list)
		#command[1:]

'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--help", dest = "help", type =str, action = "print_help")

	args = parser.parse_args()
	if (args == "--help"):
		print(prnt_help())
'''
	
	

def ehtjash_cd(location): # doesn't work yet (Path object?)
	
	try:
		if location == "":
			os.chdir("/Users/" + os.getlogin())
		else:
			os.chdir(location)
	except:
		print("ehthash cd: no file or directory found")

def ehtjash_ls():
	#Use sys.argv
	print("not yet")


def ehtjash_pwd():
	return str(os.getcwd())

#Put commands + descriptions 
def prnt_help():
	print("help segment")

if __name__ == "__main__":
	main()