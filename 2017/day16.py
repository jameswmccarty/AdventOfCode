#!/usr/bin/python



def spin(string, idx):
	out = string[:len(string)-idx]
	out = string[-idx:] + out
	return out

def exch(string, i, j):
	char1 = string[i]
	char2 = string[j]
	out = list(string)
	out[i] = char2
	out[j] = char1
	return ''.join(out)
	
def ptnr(string, p1, p2):
	idx1 = string.index(p1)
	idx2 = string.index(p2)
	out = list(string)
	out[idx1] = p2
	out[idx2] = p1
	return ''.join(out)
	

if __name__ == "__main__":

	# Part 1 Solution

	line = "abcdefghijklmnop"
	moves = []
	
	with open("day16_input", "r") as infile:
		moves = infile.read().strip().split(",")
		
	for move in moves:
		if move[0] == "s":
			line = spin(line, int(move.replace("s",'')))
		elif move[0] == "x":
			t = move.replace("x",'')
			a, b = t.split("/")
			line = exch(line, int(a), int(b))
		elif move[0] == "p":
			t = move[1:]
			a, b = t.split("/")
			line = ptnr(line, a.strip(), b.strip())
	
	print line
	
	# Part 2 Solution
	
	line = "cknmidebghlajpfo"
	seen = []
	seen.append(line)
	
	target = 1000000000
	delta = 0
	
	for i in xrange(1000):	
		for move in moves:
			if move[0] == "s":
				line = spin(line, int(move.replace("s",'')))
			elif move[0] == "x":
				t = move.replace("x",'')
				a, b = t.split("/")
				line = exch(line, int(a), int(b))
			elif move[0] == "p":
				t = move[1:]
				a, b = t.split("/")
				line = ptnr(line, a.strip(), b.strip())
		if line in seen:
			delta = i - seen.index(line) + 1
			seen.append(line)
			break
		else:
			seen.append(line)
	
	print seen[(target % 60)-1]
	
	
	
	
	
			
