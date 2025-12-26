#!/usr/bin/python


import functools

# True 1, False -1, Unk 0

def compare(l,r):
	if type(l) == type(0) and type(r) == type(0):
		if l < r:
			return 1
		if r < l:
			return -1
		return 0
	if type(l) == type([]) and type(r) == type([]):
		if len(l) == 0 and len(r) > 0:
			return 1
		while len(l) > 0 and len(r) > 0:
			check = compare(l[0],r[0])
			if check != 0:
				return check
			l,r = l[1:],r[1:]
		if len(l) == 0 and len(r) == 0:
			return 0
		elif len(l) > 0:
			return -1
		return 1
	if type(l) != type(r):
		if type(l) == type([]):
			return compare(l,[r])
		else:
			return compare([l],r)
	return 0

if __name__ == "__main__":

	# Part 1 Solution
	with open("day13_input","r") as infile:
		blocks = infile.read().split('\n\n')
	total = 0
	for idx,block in enumerate(blocks):
		l,r = block.strip().split('\n')
		nl = eval(l)
		nr = eval(r)
		if compare(nl,nr) == 1:
			total += idx+1
	print(total)

	# Part 2 Solution
	with open("day13_input","r") as infile:
		blocks = infile.read().split('\n\n')
	blocks.append("[[2]]\n[[6]]")
	signals = []
	for block in blocks:
		l,r = block.strip().split('\n')
		signals.append(eval(l))
		signals.append(eval(r))
	signals = sorted(signals,key=functools.cmp_to_key(compare),reverse=True)
	print((signals.index([[2]])+1)*(signals.index([[6]])+1))


