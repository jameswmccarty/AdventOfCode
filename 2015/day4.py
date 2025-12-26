#!/usr/bin/python

import hashlib


if __name__ == "__main__":

	# Part 1 Solution
	
	num = 0
	prefix = "yzbqklnj"
	
	m = hashlib.md5()
	
	while m.hexdigest()[0:5] != "00000":
		m = hashlib.md5()
		m.update(prefix+str(num))
		num += 1
		
	print num-1

	# Part 2 Solution
	
	num = 0
	prefix = "yzbqklnj"
	
	m = hashlib.md5()
	
	while m.hexdigest()[0:6] != "000000":
		m = hashlib.md5()
		m.update(prefix+str(num))
		num += 1
		
	print num-1
