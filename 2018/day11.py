#!/usr/bin/python


def pow(x,y,serial):
		rackID = 10 + x
		power = rackID * y
		power += serial
		power *= rackID
		power %= 1000
		power /= 100
		return power - 5	

if __name__ == "__main__":

	# Part 1 Solution
	
	serial = 8141
	
	grid = [[None] * 300 for i in range(300)]
	for x in range(300):
		for y in range(300):
			grid[y][x] = pow(x,y,serial)
	
	best = (0,0)
	mp = 0
	for i in range(300-3):
		for j in range(300-3):
			total = 0
			for x in range(3):
				for y in range(3):
					total += grid[i+x][j+y]
			if total > mp:
				mp = total
				best = (j,i)
	
	print mp
	print best
	
	# Part 2 Solution
	# Brute force and slow, but works
	best = (0,0,0)
	mp = 0
	for d in range(1,301):
		print "Testing window size " + str(d)
		for i in range(300-d):
			for j in range(300-d):
				total = 0
				for x in range(d):
					total += sum(grid[j+x][i:i+d])
				if total > mp:
					mp = total
					best = (i,j,d)

	print mp
	print best
	
	
					
	
	
