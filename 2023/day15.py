#!/usr/bin/python


def h(w):
	v = 0
	for c in w:
		v += ord(c)
		v *= 17
		v %= 256
	return v

if __name__ == "__main__":

	# Part 1 Solution
	with open("day15_input", "r") as infile:
		print(sum(h(x) for x in infile.read().strip().split(',')))

	# Part 2 Solution
	with open("day15_input", "r") as infile:
		instructions = infile.read().strip().split(',')

	hm = dict()
	for i in range(256):
		hm[i] = []

	for e in instructions:
		if '-' in e:
			l = e.replace('-','')
			i = h(l)
			for j in hm[i]:
				if j.split(' ')[0] == l:
					hm[i].remove(j)
					break
		else:
			l,v = e.split('=')
			i = h(l)
			r = -1
			for j,k in enumerate(hm[i]):
				if k.split(' ')[0] == l:
					r = j
					break
			if r == -1:
				hm[i].append(l+' '+v)
			else:
				hm[i][r] = l+' '+v
	total = 0
	for i in range(256):
		for j,v in enumerate(hm[i]):
			total += (i+1)*(j+1)*int(v.split(' ')[1])
	print(total)
