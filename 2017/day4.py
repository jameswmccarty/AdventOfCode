#!/usr/bin/python


def is_valid1(passphrase):
	passwords = passphrase.split(" ")
	while len(passwords) != 0:
		if passwords[0] in passwords[1:]:
			return False
		passwords = passwords[1:]
	return True

def is_valid2(passphrase):
	passwords = passphrase.split(" ")
	passwords = [ list(x) for x in passwords ]
	for password in passwords:
		password.sort()
	passwords = [ ''.join(x) for x in passwords ]
	while len(passwords) != 0:		
		if passwords[0] in passwords[1:]:
			return False
		passwords = passwords[1:]
	return True
	

if __name__ == "__main__":

	#Part 1 Solution

	valid = 0	
	with open("day4_input", "r") as infile:
		for line in infile.readlines():
			if is_valid1(line.strip()):
				valid += 1
	print valid

	#Part 2 Solution

	valid = 0	
	with open("day4_input", "r") as infile:
		for line in infile.readlines():
			if is_valid2(line.strip()):
				valid += 1
	print valid
