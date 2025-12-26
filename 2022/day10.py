#!/usr/bin/python


x = 1
cycle = 0
strengths = []
screen = [ ' ' ] * 240

def parse_line(line):
	pipeline = []
	global cycle,x,strengths
	if 'addx' in line:
		inst,val = line.split(' ')
		pipeline.append((1,int(val)))
	elif 'noop' in line:
		pipeline.append((0,0))
	# clock cycle
	while len(pipeline) > 0:
		cycle += 1
		if cycle == 20 or (cycle-20)%40 == 0:
			strengths.append(x*cycle)
		new_pipeline = []
		for entry in pipeline:
			timer,val = entry
			if timer == 0:
				x += val
			else:
				new_pipeline.append((timer-1,val))
		pipeline = new_pipeline

def draw_sprite(line):
	pipeline = []
	global cycle,x,screen
	if 'addx' in line:
		inst,val = line.split(' ')
		pipeline.append((1,int(val)))
	elif 'noop' in line:
		pipeline.append((0,0))
	# clock cycle
	while len(pipeline) > 0:
		if (cycle%40) == x or (cycle%40) == x-1 or (cycle%40) == x+1:
			screen[cycle] = '#'
		cycle += 1
		new_pipeline = []
		for entry in pipeline:
			timer,val = entry
			if timer == 0:
				x += val
			else:
				new_pipeline.append((timer-1,val))
		pipeline = new_pipeline

if __name__ == "__main__":

	program = []
	# Part 1 Solution
	with open("day10_input","r") as infile:
		program = [ line.strip() for line in infile.read().split('\n') ]
	for line in program:
		parse_line(line)
	print(sum(strengths))

	# Part 2 Solution
	x = 1
	cycle = 0
	for line in program:
		draw_sprite(line)
	for j in range(6):
		print(''.join(screen[40*j:40*j+40]))
