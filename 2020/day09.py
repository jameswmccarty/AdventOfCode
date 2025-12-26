#!/usr/bin/python

def verify_index(idx, offset, mem):
	for i in range(idx-offset,idx):
		for j in range(idx-offset,idx):
			if i != j and mem[i]+mem[j] == mem[idx]:
				return True
	return False

def find_weakness(mem, target):
	for window in range(2,len(mem)):
		for i in range(len(mem)):
			if sum(mem[i:i+window]) == target:
				return min(mem[i:i+window])+max(mem[i:i+window])
	return None

if __name__ == "__main__":

	# Part 1 Solution
	mem = []
	with open("day09_input", 'r') as infile:
		for line in infile.readlines():
			mem.append(int(line.strip()))
	
	weakness = None
	
	for i in range(26,len(mem)):
		if not verify_index(i, 25, mem):
			weakness = mem[i]
	print(weakness)

	# Part 2 Solution
	print(find_weakness(mem, weakness))
