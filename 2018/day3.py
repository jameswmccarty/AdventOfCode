#!/usr/bin/python


def claim_parse(claim):
	id, info = claim.split(" @ ")
	coords, dims = info.split(": ")
	x, y = coords.split(",")
	w, h = dims.split("x")
	return (str(id),int(x),int(y),int(w),int(h))


if __name__ == "__main__":
	#Part 1 Solution
	#fabric is 1000x1000 inches.  Each sq inch holds a set of claims.
	fab_size = 1000
	fabric = []
	for i in xrange(fab_size):
		fabric.append([ set() for __ in xrange(fab_size)])
	#fabric = [ [ '' ] * fab_size for i in range(fab_size) ]
	claims = []
	overlaps = 0
	with open("day3_input", "r") as infile:
		for line in infile.readlines():
			claims.append(line.strip())
	for claim in claims:
		id_num,x,y,w,h = claim_parse(claim)
		for i in range(x,x+w):
			for j in range(y,y+h):
				#fabric[j][i] = fabric[j][i] + id_num + " "
				fabric[j][i].add(id_num)
	for i in range(fab_size):
		for j in range(fab_size):
			#if len(fabric[j][i].strip().split(" ")) > 1:
			if len(fabric[j][i]) > 1:
				overlaps += 1
	print "Part 1 solution " + str(overlaps)

	#Part 2 Solution
	for claim in claims:
		valid = True
		id_num,x,y,w,h = claim_parse(claim)
		for i in range(x,x+w):
			for j in range(y,y+h):
				if len(fabric[j][i]) != 1:
					valid = False
		if valid == True:
			print "Part 2 solution " + id_num

