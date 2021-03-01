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
		command_center(command) 

def command_center(command):
	

	if command[:3] == "pwd" or command[:3] == "cwd":
		print(ehtjash_pwd())

	command_list = command.split(" ")

	if command_list[0] == "pwd" or command_list[0] == "cwd":
		print(ehtjash_pwd())
	if command_list[0] == "ls":
		subprocess.Popen(["/usr/bin/ls"] + command_list[1:])
	elif command_list[0] == "cd":
		ehtjash_cd(command_list[1])

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