import subprocess
import os
import os.path
import sys

def main():

	user = os.getlogin()
	response = input("Is this you? " + user + " ")

	'''
	pswr = input("Whats the password? ")
	'''

	while response == "yes": 
		command = input(ehtjash_pwd() + ": $ ") #we use input here in the main() for simple commands
		if command == "exit":
			break
		elif command == "help":
			prnt_help()
		elif command[:2] == "cd":
			ehtjash_cd(command[3:])
		elif command[:3] == "pwd" || command[:3] == "cwd":
			print(ehtjash_pwd())
		elif command[:2] == "ls"
			ehtjash_ls
		else:
			command_center(command) #we use sys.argv here for subprocess commands

def command_center(command):
	pass

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

def ehtjash_pwd():
	return str(os.getcwd())

#Put commands + descriptions 
def prnt_help():
	pass

if __name__ == "__main__":
	main()