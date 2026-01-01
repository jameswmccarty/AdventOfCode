#!/usr/bin/python

# Advent of Code 2025 Day 12

shapes = []

def test_fit(x_dim, y_dim, qtys):
	area = x_dim * y_dim
	if sum(len(shapes[x]) * qtys[x] for x in range(len(shapes))) > area:
		return False
	return True

if __name__ == "__main__":

	count = 0
	with open("day12_input", "r") as infile:
		for line in infile:
			if ":" in line and "x" not in line:
				shape = set()
				y = 0
			elif "#" in line or "." in line:
				for x, char in enumerate(line.strip()):
					if char == "#":
						shape.add((x, y))
				y += 1
			elif len(line.strip()) == 0:
				shapes.append(shape)
			elif "x" in line:
				dims, qtys = line.strip().split(": ")
				x_dim, y_dim = map(int, dims.split("x"))
				qtys = [ int(x) for x in qtys.split(" ") ]
				if test_fit(x_dim, y_dim, qtys):
					count += 1
	print(count)

