#!/usr/bin/python

import md5

decoder = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15 }

if __name__ == "__main__":

	# Part 1 Solution
	
	door_id = 'reyedfim'
	counter = 0
	password = ''
	
	while len(password) < 8:
		m = md5.new()
		m.update(door_id+str(counter))
		if "00000" == m.hexdigest()[0:5]:
			password += m.hexdigest()[5]
		counter += 1
	
	print password
	
	# Part 2 Solution
	
	password = [None] * 8
	counter = 0
	
	while None in password:
		m = md5.new()
		m.update(door_id+str(counter))
		hd = m.hexdigest()
		if "00000" == hd[0:5]:
			if decoder[hd[5]] < len(password) and password[decoder[hd[5]]] == None:
				password[decoder[hd[5]]] = hd[6]
		counter += 1
		
	print ''.join(password)
	
