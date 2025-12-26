#!/usr/bin/python

import functools

def FFT(n, phases):
	base = [0,1,0,-1]
	phase_keys = []
	for idx in range(len(n)):
		key = []
		b_idx = 0
		while len(key) < len(n)+1:
			key += [base[b_idx%len(base)]] * (idx+1)
			b_idx += 1
		key = key[1:len(n)+1]
		phase_keys.append(key)
	for p in range(phases):
		next = []
		for i in range(len(n)):
			val = 0
			for x in range(len(n)):
				val += n[x] * phase_keys[i][x]
			next.append(abs(val)%10)
		n = next
	return n
	

if __name__ == "__main__":

	# Part 1 Solution
	with open('day16_input', 'r') as infile:
		n = infile.readline()	
	n = [ int(x) for x in n.strip() ]
	print(''.join(str(i) for i in FFT(n,100)[0:8]))

	# Part 2 Solution
	"""
	Technique borrowed from /u/Diderikdm/ on AOC reddit post.
	"""
	with open('day16_input', 'r') as infile:
		n = infile.readline().strip()*10000
	i = (n[int(n[0:7]):])
	for a in range(100):
		string = '' 
		e = 0
		while e < len(i):
		    if e == 0:
		        total = 0
		        for f in i:
		            total += int(f)
		    elif e > 0:
		        total -= int(i[e-1])
		    string += str(total)[-1]
		    e += 1
		i = string
	print(i[0:8]) 


