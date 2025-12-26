#!/usr/bin/python


def dragon_fill(a, size):
	while len(a) < size:
		b = a[::-1]
		b = b.replace("0", ".")
		b = b.replace("1", "0")
		b = b.replace(".", "1")
		a += "0" + b
	return a[0:size]
	
def checksum(a):
	out = ''
	for i in range(0,len(a),2):
		if a[i]==a[i+1]:
			out += "1"
		else:
			out += "0"
	if len(out) % 2 == 0:
		return checksum(out)
	return out

if __name__ == "__main__":

	# Part 1 Solution

	#print checksum(dragon_fill('10000', 20))		
	print checksum(dragon_fill('11110010111001001', 272))

	# Part 2 Solution
	print checksum(dragon_fill('11110010111001001', 35651584))
