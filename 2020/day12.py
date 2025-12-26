#!/usr/bin/python


pos = (0,0)
wpt = (10,1)
#           E,S,W,N
headings = [0,1,2,3]
heading = 0

def do_cmd(cmd):

	global heading
	global pos

	action, value = cmd[0], int(cmd[1:])
	
	if action == "L" or action == "R":
		idx = headings[heading]
		while(value) > 0:
			if action == "L":
				idx -= 1
			else:
				idx += 1
			idx = idx % 4
			value -= 90
		heading = headings[idx]
		return
	
	if action == "F":
		action = ["E","S","W","N"][heading]
	
	if action == "N":
		pos = (pos[0],pos[1]+value)
	elif action == "S":
		pos = (pos[0],pos[1]-value)
	elif action == "E":
		pos = (pos[0]+value,pos[1])
	elif action == "W":
		pos = (pos[0]-value,pos[1])

def do_waypoint(cmd):

	global pos
	global wpt

	action, value = cmd[0], int(cmd[1:])
	
	if action == "L" or action == "R":
		if action == "L":
			value = 360 - (value%360)
			action = "R"
		while(value) > 0:
			wpt = (wpt[1],-wpt[0])
			value -= 90
		return
	
	if action == "F":
		pos = (pos[0]+wpt[0]*value,pos[1]+wpt[1]*value)
		return
	
	if action == "N":
		wpt = (wpt[0],wpt[1]+value)
	elif action == "S":
		wpt = (wpt[0],wpt[1]-value)
	elif action == "E":
		wpt = (wpt[0]+value,wpt[1])
	elif action == "W":
		wpt = (wpt[0]-value,wpt[1])


if __name__ == "__main__":

	cmds = []

	# Part 1 Solution
	with open("day12_input", 'r') as infile:
		for line in infile.readlines():
			cmds.append(line.strip())
	for cmd in cmds:
		do_cmd(cmd)
	print(abs(pos[0])+abs(pos[1]))


	# Part 2 Solution
	pos = (0,0)
	for cmd in cmds:
		do_waypoint(cmd)
	print(abs(pos[0])+abs(pos[1]))
