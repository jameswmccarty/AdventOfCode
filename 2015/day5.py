#!/usr/bin/python



# lower case
doubles = [ chr(x)+chr(x) for x in range(97,123) ]

illegals = ['ab', 'cd', 'pq', 'xy']

def ill(word):
	for pair in illegals:
		if pair in word:
			return True
	return False

def dbl(word):
	for pair in doubles:
		if pair in word:
			return True
	return False

def vowel(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	return sum(word.count(x) for x in vowels)
	
def split_ltr(word):
	for i in range(len(word)-2):
		if word[i] == word[i+2]:
			return True
	return False
	
def paired(word):
	while len(word) > 2:
		pair = word[0:2]
		if pair in word[2:]:
			return True
		word = word[1:]
	return False		

if __name__ == "__main__":

	# Part 1 Solution
	
	words = []
	nice = 0
	with open("day5_input", "r") as infile:
		for line in infile.readlines():
			words.append(line.strip())
	
	for word in words:
		if not ill(word) and dbl(word) and vowel(word) >= 3:
			nice += 1
	print nice
	
	# Part 2 Solution
	nice = 0
	for word in words:
		if paired(word) and split_ltr(word):
			nice += 1
	print nice
	
	

	
	
