#!/usr/bin/python


# wrapping paper
def sq_total(dim):
	l,w,h = dim
	return 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)

def ribbon(dim):
	l,w,h = dim
	return 2*min(l+w,w+h,l+h) + l*w*h

if __name__ == "__main__":

	dims = []

	# Part 1 Solution
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			dims.append(tuple(map(int,line.strip().split("x"))))

	print(sum(map(sq_total,dims)))

	# Part 2 Solution
	print(sum(map(ribbon,dims)))
