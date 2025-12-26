#!/usr/bin/python


illegals = ['i', 'o', 'l']
pairs    = { chr(i)+chr(i) for i in range(97,123) }

def straight(word):
	for i in range(len(word)-2):
		if word[i+1] == chr(ord(word[i])+1) and word[i+2] == chr(ord(word[i])+2):
			return True
	return False
	
def doubled(word):
	for pair1 in pairs:
		if pair1 in word:
			for pair2 in pairs.difference({pair1}):
				if pair2 in word:
					return True
	return False
	
def inc_password(word, idx):
	word = list(word)
	if idx < 0 or idx > len(word)-1:
		return ''.join(word)
	nxt = chr((ord(word[idx])-96) % 26 + 97)
	while nxt in illegals:
		nxt = chr((ord(nxt)-96) % 26 + 97)
	word[idx] = nxt
	if word[idx] == 'a':
		return inc_password(word, idx-1)
	else:
		return ''.join(word)
	
def legal(word):
	if straight(word) and doubled(word):
		return True
	return False
	
if __name__ == "__main__":

	# Part 1 Solution
	
	word = "cqjxjnds"
	
	while not legal(word):
		word = inc_password(word, len(word)-1)
	print word
	
	# Part 2 Solution
	
	word = inc_password(word, len(word)-1)
	while not legal(word):
		word = inc_password(word, len(word)-1)
	print word
	
