#!/usr/bin/python


def seq_next(seq):
	if set(seq) == {0}:
		return 0
	return seq[-1] + seq_next( [ seq[i]-seq[i-1] for i in range(1,len(seq)) ] )
	

if __name__ == "__main__":

	# Part 1 Solution
	with open("day09_input", "r") as infile:
		print(sum(seq_next( [ int(x) for x in line.strip().split() ] ) for line in infile ))


	# Part 2 Solution
	with open("day09_input", "r") as infile:
		print(sum(seq_next( [ int(x) for x in line.strip().split() ][::-1] ) for line in infile ))
