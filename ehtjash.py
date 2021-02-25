import subprocess
import os
import os.path
import sys

def main():

	user = os.getlogin()
	response = input("Is this you? " + user)

	while response == "yes": 
		command = input(ehtjash_pwd() + ": $ ") #we use input here in the main() for simple commands
		if command == "exit":
			break
		elif command == "help":
			prnt_help()
		elif command[:3] == "cd":
			ehtjash_cd(command[3:])
		elif command[:3] == "pwd":
			print(ehtjash_pwd())
		else:
			command_center(command) #we use sys.argv here for subprocess commands




def command_center(command):
	pass

def ehtjash_cd(location): # doesn't work yet (Path object?)
	
	try:
		os.chdir("/home/henry/Documents")
	except NotADirecoryError:
		print("ehthash cd: no file or directory found")

def ehtjash_pwd():
	return str(os.getcwd())

def prnt_help():
	pass

if __name__ == "__main__":
	main()