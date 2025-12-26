#!/usr/bin/python

def move(current, cups):
	s = cups.index(current)
	pick_up = [ cups[i%len(cups)] for i in range(s+1,s+4) ]
	dest = current - 1
	if dest < min(cups):
		dest = max(cups)
	while dest in pick_up:
		dest -= 1
		if dest < min(cups):
			dest = max(cups)

	for cup in pick_up:
		cups.remove(cup)
	
	insert = cups.index(dest)
	cups = cups[0:insert+1] + pick_up + cups[insert+1:]
	return cups[(cups.index(current)+1)%len(cups)], cups


if __name__ == "__main__":

	# Part 1 Solution

	#labeling = "389125467"
	labeling = "614752839"
	cups = [ int(x) for x in labeling ]
	next = cups[0]
	for i in range(100):
		next, cups = move(next, cups)
	out = ''
	for i in range(1,9):
		out += str(cups[(cups.index(1)+i)%len(cups)])
	print(out)

	# Part 2 Solution
	
	cups = dict()
	
	#labeling = "389125467"
	
	for i, char in enumerate(labeling):
		cups[int(char)] = int(labeling[(i+1)%len(labeling)])
	cups[int(labeling[-1])] = 10
	for i in range(len(labeling)+1,1000000):
		cups[i] = i+1
	cups[1000000] = int(labeling[0])

	low_cup = 1
	hi_cup  = 1000000
	current = int(labeling[0])
	
	for _ in range(10000000):
		a,b,c = cups[current], cups[cups[current]], cups[cups[cups[current]]]
		cups[current] = cups[cups[cups[cups[current]]]]
		dest = current - 1
		if dest < low_cup:
			dest = hi_cup
		while dest in (a,b,c):
			dest -= 1
			if dest < low_cup:
				dest = hi_cup
		#print("Move ", _+1, current, dest, a, b, c)
		t = cups[dest]
		cups[dest] = a
		cups[c] = t
		current = cups[current]
	print(cups[cups[1]]*cups[1])
