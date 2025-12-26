#!/usr/bin/python


import copy

class Brick:
	
	def __init__(self, init_string=None):
		self.volume = set()
		self.fell  = False
		if init_string == None:
			return
		a,b = init_string.split('~')
		x1,y1,z1 = (int(x) for x in a.split(','))
		x2,y2,z2 = (int(x) for x in b.split(','))
		for z in range(min(z1,z2),max(z1,z2)+1):
			for y in range(min(y1,y2),max(y1,y2)+1):
				for x in range(min(x1,x2),max(x1,x2)+1):
					self.volume.add((x,y,z))

	def footprint_bounds(self):
		x_min = min( t[0] for t in self.volume )
		x_max = max( t[0] for t in self.volume ) + 1
		y_min = min( t[1] for t in self.volume )
		y_max = max( t[1] for t in self.volume ) + 1
		return ((x_min,y_min),(x_max,y_max))

	def footprint(self):
		return { (x,y) for x,y,z in self.volume }

	def ceiling(self):
		return max( t[2] for t in self.volume )
	
	def floor(self):
		return min( t[2] for t in self.volume )

	# move the brick as low as possible by looking at any bricks below this one
	def drop(self,other_bricks):
		if 1 in { t[2] for t in self.volume }:
			return False
		other_bricks = [ b for b in other_bricks if b != self ]
		footy = self.footprint()
		other_bricks = [ b for b in other_bricks if len(footy.intersection(b.footprint())) > 0 ]
		collision_volume = set()
		for b in other_bricks:
			for e in b.volume:
				collision_volume.add(e)
		moved = False
		while 1 not in { t[2] for t in self.volume }:
			new_volume = { (x,y,z-1) for x,y,z in self.volume }
			if len(new_volume.intersection(collision_volume)) == 0:
				moved = True
				self.fell = True
				self.volume = new_volume
			else:
				return moved
		return moved

	# determine if it is possible to move a block down by 1 square
	def bump(self,global_volume):
		if 1 in { t[2] for t in self.volume }:
			return False
		for e in self.volume:
			global_volume.discard(e)
		new_volume = { (x,y,z-1) for x,y,z in self.volume }
		if len(new_volume.intersection(global_volume)) == 0:
			return True
		return False

	# move the brick down one square if possible
	def bump2(self,other_bricks):
		if 1 in { t[2] for t in self.volume }:
			return
		other_bricks = [ b for b in other_bricks if b != self ]
		new_volume = { (x,y,z-1) for x,y,z in self.volume }
		if all( len(new_volume.intersection(b.volume)) == 0 for b in other_bricks):
			self.fell = True
			self.volume = new_volume

if __name__ == "__main__":

	bricks = []
	# Part 1 Solution
	with open("day22_input", "r") as infile:
		for line in infile:
			b = Brick(line.strip())
			bricks.append(b)

	# compress stack
	for i in range(1,max( b.ceiling() for b in bricks)):
		chunk = [ b for b in bricks if i in { t[2] for t in b.volume } ]
		while any( b.drop(bricks) for b in chunk ):
			continue

	global_volume = set()
	for b in bricks:
		for e in b.volume:
			global_volume.add(e)

	brick_count = 0
	excludes = set()
	for i in range(len(bricks)):
		current_volume = { x for x in global_volume }
		trial_stack = [ copy.copy(b) for b in bricks ]
		removed = trial_stack.pop(i)
		for e in removed.volume:
			current_volume.discard(e)
		if not any( b.bump(copy.copy(current_volume)) for b in trial_stack ):
			brick_count += 1
			excludes.add(i)
	print(brick_count)

	# Part 2 Solution

	brick_count = 0
	for j in range(len(bricks)):
		if j not in excludes:
			trial_stack = [ copy.copy(b) for b in bricks ]
			for b in trial_stack:
				b.fell = False
			removed = trial_stack.pop(j)
			# compress stack, but only by 1 movement per brick
			for i in range(1,max( b.ceiling() for b in trial_stack )):
				chunk = [ b for b in trial_stack if i in { t[2] for t in b.volume } and not b.fell ]
				[ b.bump2(trial_stack) for b in chunk ]
			brick_count += sum( b.fell for b in trial_stack )
	print(brick_count)
