#!/usr/bin/python


def valid_password1(line):
	rule, letter, password = line.split(" ")
	lo, hi = rule.split("-")
	letter = letter.replace(":",'')
	if password.count(letter) >= int(lo) and password.count(letter) <= int(hi):
		return True
	return False

def valid_password2(line):
	rule, letter, password = line.split(" ")
	lo, hi = rule.split("-")
	letter = letter.replace(":",'')
	if (password[int(lo)-1] == letter) ^ (password[int(hi)-1] == letter):
		return True
	return False

if __name__ == "__main__":

	# Part 1 Solution
	
	with open("day02_input", 'r') as infile:
		print(sum([valid_password1(line) for line in infile.readlines()]))


	# Part 2 Solution
	
	with open("day02_input", 'r') as infile:
		print(sum([valid_password2(line) for line in infile.readlines()]))

