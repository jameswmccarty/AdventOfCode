#!/usr/bin/python

def rng():
	seed = 20151125
	yield seed
	while True:
		seed *= 252533
		seed %= 33554393
		yield seed
		
def seq_num(row, col):
	count = 0
	step =  1
	while True:
		for j in range(1,step+1):
			count += 1
			if step-j+1 == row and j == col:
					return count
		step += 1

if __name__ == "__main__":

	# Part 1 Solution

	z = rng()

	for i in range(seq_num(2978,3083)):
		soln = z.next()
	print soln
