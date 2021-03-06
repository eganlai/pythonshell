import subprocess
import os
from colorama import init, Fore, Back
#import sys
#import argparse

def main():

	while True: 
		command = input(ehtjash_pwd() + ": " + Fore.GREEN + "$ " + Fore.WHITE)
		if command == "exit":
			break
		elif command == "--help":
			prnt_help()
		else:
			command_list = command.split("|")
		command_center(command_list, None)

def command_center(command_list, stIn):

	command = command_list[0].split(" ")
	for i in range(len(command) - 1): #take out any empty strings
		if command[i] == "":
			del command[i]

	if stIn is not None:
		command.append(stIn)
	
	if len(command_list) > 1:
		command_center(command_list[1:], commands(command))
	commands(command)

'''
	parser = argparse.ArgumentParser()
	parser.add_argument("--help", dest = "help", type =str, action = "print_help")

	args = parser.parse_args()
	if (args == "--help"):
		print(prnt_help())
'''
	
	
def commands(command_list):
	if command_list[0] == "pwd" or command_list[0] == "cwd":
		return ehtjash_pwd()
	elif command_list[0] == "cd":
		ehtjash_cd(command_list[1])
	else:
		try:
			return subprocess.Popen(command_list)
		except FileNotFoundError:
			print("Command Not Found (。_。)")

def ehtjash_cd(location): # doesn't work yet (Path object?)
	
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