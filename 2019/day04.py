#!/usr/bin/python


def valid1(password):
	paired = False
	for pair in ['00','11','22','33','44','55','66','77','88','99']:
		if pair in str(password):
			paired = True
	if paired:
		for i in range(5):
			if int(str(password)[i]) > int(str(password)[i+1]):
				return False
		return True
	return False

def valid2(password):
	paired = False
	for pair in ['00','11','22','33','44','55','66','77','88','99']:
		if pair in str(password) and pair+pair[0] not in str(password):
			paired = True
	if paired:
		for i in range(5):
			if int(str(password)[i]) > int(str(password)[i+1]):
				return False
		return True
	return False

if __name__ == "__main__":
	
	# Part 1 Solution
	total = 0
	for i in range(136760,595730+1):
		if valid1(i):
			total += 1
	print(total)
	
	# Part 2 Solution
	total = 0
	for i in range(136760,595730+1):
		if valid2(i):
			total += 1
	print(total)


