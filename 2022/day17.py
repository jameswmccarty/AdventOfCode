#!/usr/bin/python


stopped = set()
moves = ''
move_idx = 0
max_height = 0

class shape:

	shape_offsets = [ { (0,0),(1,0),(2,0),(3,0) },
				{ (1,2),(0,1),(1,1),(2,1),(1,0) },
				{ (2,2),(2,1),(0,0),(1,0),(2,0) },
				{ (0,0),(0,1),(0,2),(0,3) },
				{ (0,0),(1,0),(0,1),(1,1) } ]

	def next_start(self):
		global stopped, max_height
		if len(stopped) == 0:
			return (2,4)
		return(2,max_height+4)

	def __init__(self,order):
		self.coords = set()
		self.order = order
		x,y = self.next_start()
		for dx,dy in self.shape_offsets[order%5]:
			self.coords.add((x+dx,y+dy))

	def move(self):
		global stopped, moves, move_idx, max_height
		d = moves[move_idx%len(moves)]
		move_idx += 1
		# Move right or left
		if d == '>':
			check_shift = { (x+1,y) for x,y in self.coords }
			if not (len(check_shift.intersection(stopped)) > 0 or any( [ x > 6 for x,y in check_shift ] )):
				self.coords = check_shift
		elif d == '<':
			check_shift = { (x-1,y) for x,y in self.coords }
			if not (len(check_shift.intersection(stopped)) > 0 or any( [ x < 0 for x,y in check_shift ] )):
				self.coords = check_shift
		# Try to move down.  If blocked, don't move and stop.
		check_shift = { (x,y-1) for x,y in self.coords }
		if not (len(check_shift.intersection(stopped)) > 0 or any( [ y == 0 for x,y in check_shift ] )):
			self.coords = check_shift
			return True
		else:
			stopped.update(self.coords)
			max_height = max(max_height,max([ y for x,y in self.coords]))
			return False

if __name__ == "__main__":

	# Part 1 Solution
	with open('day17_input','r') as infile:
		moves = infile.read().strip()

	shape_count = 0
	while shape_count != 2022:
		current_shape = shape(shape_count)
		while current_shape.move():
			continue
		shape_count += 1
	print(max_height)

	# Part 2 Solution
	max_height = 0
	stopped = set()
	shape_count = 0
	move_idx = 0
	heights_at_shapes = dict()
	heights_at_states = dict()
	counts_at_states  = dict()
	seen = set()
	while True:
		current_shape = shape(shape_count)
		while current_shape.move(): # drop the next shape
			continue
		key = (shape_count % 5, move_idx%len(moves))
		if key in seen:
			if len(heights_at_states[key]) >= 2:
				delta = heights_at_states[key][-1] - heights_at_states[key][-2]
				rocks_needed = 1000000000000 - shape_count
				cycle_size = counts_at_states[key][-1] - counts_at_states[key][-2]
				if rocks_needed % cycle_size == 0:
					total = max_height + delta*rocks_needed//cycle_size
					print(total-1)
					break
		seen.add(key)
		if key in heights_at_states:
			heights_at_states[key].append(max_height)
		else:
			heights_at_states[key] = [max_height]
		if key in counts_at_states:
			counts_at_states[key].append(shape_count)
		else:
			counts_at_states[key] = [shape_count]
		shape_count += 1
