import subprocess
import os
import sys

def main():
	while True: 
		command = input("$ ") #we use input here in the main() for simple commands
		if command == "exit":
			break
		elif command == "help":
			prnt_help()
		elif command[:3] == "cd":
			ehtjash_cd(command[3:])
		elif command[:3] == "pwd":
			ehtjash_pwd()
		else:
			command_center(command) #we use sys.argv here for subprocess commands


def command_center(command):
	pass

def ehtjash_cd(location): # doesn't work
	try:
		os.chdir(os.path.abspath(location))
	except Exception:
		print("ehthash cd: no file or directory found")

def ehtjash_pwd():
	print(os.getcwd())

def prnt_help():
	pass

if __name__ == "__main__":
	main()