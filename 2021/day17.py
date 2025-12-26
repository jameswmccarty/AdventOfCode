#!/usr/bin/python


if __name__ == "__main__":

	# stores at starting x vel:
	# (min steps to reach target, max steps to reach target)	
	x_step_ranges = dict()	
	
	y_vel_steps = dict()


	"""
	In order to land in bounds, you need to conduct a throw so that the x value
	lands in bounds, and the y value does not overshoot.
	
	The x position will equal x+(x-1)+(x-2)+...+(x-x) and stop.  You should try to find a triangle number that falls
	within the x bounds.
	
	The next step is to find a y that won't overshoot.  In the example, the upper box bound is -10.  Find the sum of
	9+(9-1)+...+0 to find the max height.
	"""
		
	def max_height(y_upper_bound):
		y_upper_bound = abs(y_upper_bound) - 1
		return y_upper_bound*(y_upper_bound+1)//2
	
	def find_starting_x_poss(lo,hi):
		for t in range(1,lo):
			pos = 0
			steps = 0
			vel = t
			lo_steps = float('inf')
			hi_steps = 0
			hit = False
			while vel >= 0 and pos < hi:
				pos += vel
				steps += 1
				vel -= 1
				if pos >= lo and pos <= hi:
					hit = True
					lo_steps = min(steps,lo_steps)
					hi_steps = max(steps,hi_steps)
					if vel == 0:
						hi_steps = float('inf')
			if hit:
				x_step_ranges[t] = (lo_steps,hi_steps)

	def find_y_series_steps(lo,hi):
		for t in range(lo+1,-hi):
			pos = 0
			steps = 0
			vel = t
			lo_steps = float('inf')
			hi_steps = 0
			hit = False
			while pos >= hi:
				pos += vel
				steps += 1
				vel -= 1
				if pos <= lo and pos >= hi:
					hit = True
					lo_steps = min(steps,lo_steps)
					hi_steps = max(steps,hi_steps)
			if hit:
				y_vel_steps[t] = (lo_steps,hi_steps)

		
	# Part 1 Solution
	with open("day17_input","r") as infile:
		problem = infile.read().strip()
	x_range,y_range = problem.split(",")
	x_range = x_range[15:]
	y_range = y_range[3:]
	y_up,y_lo = y_range.split("..")
	x_lo,x_hi = x_range.split("..")
	# make sure to sort the input so that y_lo is the lowest of the two
	print(max_height(int(y_lo)))


	# Part 2 Solution
	
	find_starting_x_poss(int(x_lo),int(x_hi))
	find_y_series_steps(int(y_up),int(y_lo))
	combos = set()
	total = 0
	for x,value in x_step_ranges.items():
		x_low,x_high = value
		for y,y_range in y_vel_steps.items():
			y_min,y_max = y_range
			for z in range(y_min,y_max+1):
				if z >= x_low and z <= x_high:
					total += 1
					combos.add((x,y))
	# The number of points in the area of the target can be added to the 
	# list of valid combos
	print((int(x_hi)+1-int(x_lo))*(int(y_up)+1-int(y_lo))+len(combos))

