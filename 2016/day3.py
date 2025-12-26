#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	
	valid = 0
	
	with open("day3_input", "r") as infile:
		for line in infile.readlines():
			sides = line.lstrip().strip().split("  ")
			sides = [int(x) for x in sides if x != '']
			sides.sort()
			if sides[0] + sides[1] > sides[2]:
				valid += 1
	print valid
			
	# Part 2 Solution
	
	valid = 0
	
	with open("day3_input", "r") as infile:
		while True:
			row1 = infile.readline()
			if row1 == '':
				break
			row2 = infile.readline()
			row3 = infile.readline()
			row1 = row1.lstrip().strip().split("  ")
			row2 = row2.lstrip().strip().split("  ")
			row3 = row3.lstrip().strip().split("  ")
			row1 = [int(x) for x in row1 if x != '']
			row2 = [int(x) for x in row2 if x != '']
			row3 = [int(x) for x in row3 if x != '']
		
			for i in range(3):
				tri_poss = [ row1[i], row2[i], row3[i] ]
				tri_poss.sort()
				if tri_poss[0] + tri_poss[1] > tri_poss[2]:
					valid += 1
					
	print valid
			
