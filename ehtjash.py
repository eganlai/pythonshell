import subprocess
import os
import sys

def main():
	while True: 
		command = input("$ ")
		if command == "exit":
			break
		elif command == "help":
			print_help()
		elif command[:3] == "cd":
			ehtjash_cd(command[3:])
		elif command[:3] == "pwd":
			ehtjash_pwd()
		else:
			command_center(command)


def command_center():
	pass

def ehtjash_cd(location):
	try:
		os.chdir() #figure out what goes in here
	except Exception:
		print("ehthash cd: no file or directory found")

def ehtjash_pwd():
	print(os.getcwd())

def print_help()
	pass

if __name__ == "__main__":
	main()