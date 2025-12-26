#!/usr/bin/python



class RNG:

	def __init__(self, factor, seed):
		self.factor = factor
		self.seed = seed
		
	def next(self):
		self.seed *= self.factor
		self.seed %= 2147483647
		return self.seed

class RNG_2:

	def __init__(self, factor, seed, mod):
		self.factor = factor
		self.seed = seed
		self.mod = mod
		
	def next(self):
		self.seed *= self.factor
		self.seed %= 2147483647
		while self.seed % self.mod != 0:
			self.seed *= self.factor
			self.seed %= 2147483647
		return self.seed		

if __name__ == "__main__":

	# Test Cases
	#a = RNG(16807, 65)
	#b = RNG(48271, 8921)

	# Part 1
	a = RNG(16807, 516)
	b = RNG(48271, 190)
	
	# Part 2
	#a = RNG_2(16807, 65,  4)
	#b = RNG_2(48271, 8921,8)	
	
	a = RNG_2(16807, 516, 4)
	b = RNG_2(48271, 190, 8)

	matches = 0	
	for i in range(40000000):
		if( (a.next() & 0xFFFF) ==  (b.next() & 0xFFFF) ):
			matches += 1
	print matches

	matches = 0
	for i in range(5000000):
		if( (a.next() & 0xFFFF) ==  (b.next() & 0xFFFF) ):
			matches += 1
	print matches
