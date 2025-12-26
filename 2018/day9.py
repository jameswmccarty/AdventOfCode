#!/usr/bin/python


class Marble:

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
		
class Circle:

	def __init__(self):
		self.head = None
	
	def insert(self, value):
		marble = Marble(value)
		
		# first addition
		if self.head == None:
			self.head = marble
			marble.next = marble
			marble.prev = marble
			return 0
		# special case divisible by 23
		elif marble.value % 23 == 0:
			# find marble 7 counter-clockwise from heaad
			for i in range(7):
				self.head = self.head.prev
			retval = marble.value + self.head.value
			# new head is clockwise to marble to remove
			self.head = self.head.next
			# prune out node to remove
			self.head.prev = self.head.prev.prev
			self.head.prev.next = self.head
			return retval
		# normal insert
		else:
			l = self.head.next
			r = self.head.next.next
			l.next = marble
			marble.prev = l
			r.prev = marble
			marble.next = r
			self.head = marble
			return 0

if __name__ == "__main__":

	#Part 1 Solution
	
	num_players = 432
	next_marble = 0
	max_marbles = 71019 
	scores = [0] * num_players
	turn = 0
	circle = Circle()
	circle.insert(next_marble)
	
	while next_marble < max_marbles:
		next_marble += 1
		scores[turn] += circle.insert(next_marble)
		turn += 1
		turn %= len(scores)
	
	print max(scores)
	
	# Part 2 Solution
	num_players = 432
	next_marble = 0
	max_marbles = 71019*100
	scores = [0] * num_players
	turn = 0
	circle = Circle()
	circle.insert(next_marble)
	
	while next_marble < max_marbles:
		next_marble += 1
		scores[turn] += circle.insert(next_marble)
		turn += 1
		turn %= len(scores)
	
	print max(scores)
		
	
