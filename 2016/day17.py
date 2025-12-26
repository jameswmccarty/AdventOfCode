#!/usr/bin/python

from collections import deque
from hashlib import md5


unlocked = { 'b', 'c', 'd', 'e', 'f' }

def bfs(dest_x, dest_y, salt):
	search_queue = deque()
	search_queue.append(((0,0),''))
	while len(search_queue) > 0:
		posit, path = search_queue.popleft()
		x, y = posit
		if x == dest_x and y == dest_y:
			return path
		m = md5()
		m.update(salt+path)
		key = m.hexdigest()[0:4]
			
		if x > 0 and key[2] in unlocked:
			search_queue.append(((x-1,y), path+'L'))
		if y > 0 and key[0] in unlocked:
			search_queue.append(((x,y-1), path+'U'))
		if y < 3 and key[1] in unlocked:
			search_queue.append(((x,y+1), path+'D'))
		if x < 3 and key[3] in unlocked:
			search_queue.append(((x+1,y), path+'R'))
	
	return float('inf') # no solution
	
def longest_bfs(dest_x, dest_y, salt):
	search_queue = deque()
	search_queue.append(((0,0),''))
	max_len = 0
	while len(search_queue) > 0:
		posit, path = search_queue.popleft()
		x, y = posit
		if x == dest_x and y == dest_y:
			max_len = max(max_len, len(path))
		else:
			m = md5()
			m.update(salt+path)
			key = m.hexdigest()[0:4]
				
			if x > 0 and key[2] in unlocked:
				search_queue.append(((x-1,y), path+'L'))
			if y > 0 and key[0] in unlocked:
				search_queue.append(((x,y-1), path+'U'))
			if y < 3 and key[1] in unlocked:
				search_queue.append(((x,y+1), path+'D'))
			if x < 3 and key[3] in unlocked:
				search_queue.append(((x+1,y), path+'R'))
	
	return max_len

if __name__ == "__main__":

	# Part 1 Solution
	
	print bfs(3,3,'bwnlcvfs')
	
	# Part 2 Solution
	
	print longest_bfs(3, 3, 'bwnlcvfs')
