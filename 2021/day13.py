#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution

	instructions = []
	dots = set()

	def fold(dots,inst):
		axis,units = inst
		new_dots = set()
		if axis == "y":
			for dot in dots:
				if dot[1] > units:
					new_dots.add((dot[0],dot[1]-2*(dot[1]-units)))
				else:
					new_dots.add(dot)
		elif axis == "x":
			for dot in dots:
				if dot[0] > units:
					new_dots.add((dot[0]-2*(dot[0]-units),dot[1]))
				else:
					new_dots.add(dot)
		return new_dots

	with open("day13_input","r") as infile:
		for line in infile.readlines():
			if "," in line:
				x,y = line.strip().split(",")
				dots.add((int(x),int(y)))
			elif line.strip() == '':
				continue
			elif "fold" in line:
				instruction,value = line.strip().split("=")
				instructions.append((instruction[-1],int(value)))

	dots = fold(dots,instructions[0])
	print(len(dots))

	# Part 2 Solution

	instructions = instructions[1:]
	while len(instructions) > 0:
		dots = fold(dots,instructions[0])
		instructions = instructions[1:]

	for j in range(max([ x[1] for x in dots ])+1):
		for i in range(max([ x[0] for x in dots ])+1):
			if (i,j) in dots:
				print("#",end='')
			else:
				print(" ",end='')
		print()

