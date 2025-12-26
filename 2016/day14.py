#!/usr/bin/python

from hashlib import md5


hash_dict = dict() # cache stretched hashes for speed

def stretch_hash(hash):
	for i in range(2016):
		m = md5()
		m.update(hash)
		hash = m.hexdigest()
	return hash

def valid__stretch_key(salt, index):
	if index not in hash_dict:
		m = md5()
		m.update(salt+str(index))
		hash_dict[index] = stretch_hash(m.hexdigest())
	digest = hash_dict[index]
	triple_char = None	
	for i in range(len(digest)-2):
		if digest[i]==digest[i+1]==digest[i+2]:
			triple_char = digest[i]
			break
	if triple_char == None:
		return False
	for sub_idx in range(1,1001):
		if index+sub_idx not in hash_dict:
			m = md5()
			m.update(salt+str(index+sub_idx))
			hash_dict[index+sub_idx] = stretch_hash(m.hexdigest())
		digest = hash_dict[index+sub_idx]
		if triple_char*5 in digest:
			return True
	return False

def valid_key(salt, index):
	m = md5()
	m.update(salt+str(index))
	digest = m.hexdigest()	
	triple_char = None	
	for i in range(len(digest)-2):
		if digest[i]==digest[i+1]==digest[i+2]:
			triple_char = digest[i]
			break
	if triple_char == None:
		return False
	# print "Index", index, " produces a tripple of ", triple_char
	for sub_idx in range(1,1001):
		m = md5()
		m.update(salt+str(index+sub_idx))
		if triple_char*5 in  m.hexdigest():
			return True
	return False

if __name__ == "__main__":

	# Part 1 Solution

	#salt = 'abc'
	salt = 'ihaygndm'
	index = -1
	counter = 0
	while counter < 64:
		index += 1
		if valid_key(salt, index):
			counter += 1
	print index
	
	# Part 2 Solution
	
	index = -1
	counter = 0
	while counter < 64:
		index += 1
		if valid__stretch_key(salt, index):
			counter += 1
	print index
