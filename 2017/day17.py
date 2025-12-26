#!/usr/bin/python



class RingBuf:

	def __init__(self, step):
		self.contents = [0]
		self.step = step
		self.pos = 0
		self.next = 1
		
	def insert(self):
		self.pos = (self.pos + self.step) % len(self.contents)
		self.contents.insert(self.pos+1, self.next)
		self.pos = self.contents.index(self.next)
		self.next += 1
		
if __name__ == "__main__":

	# Part 1 Solution
	
	a = RingBuf(382)
	
	for i in range(2017):
		a.insert()
	print a.contents[a.pos+1]
	
	# Part 2 Solution
	
	step = 382
	length = 1
	pos    = 0
	next   = 1
	after_zero = None
	
	for i in xrange(50000000):
		pos += step
		pos %= length
		pos += 1
		length += 1
		if pos == 1:
			after_zero = next
		next += 1
	print after_zero
	
