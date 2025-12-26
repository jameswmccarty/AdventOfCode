#!/usr/bin/python

if __name__ == "__main__":

	earliest = None
	fastest  = float('inf')
	fast_id  = None
	schedule = []

	# Part 1 Solution
	with open("day13_input", 'r') as infile:
		earliest = int(infile.readline())
		for entry in infile.readline().split(","):
			entry = entry.strip()
			if entry != '' and entry != 'x':
				schedule.append(int(entry))
	for entry in schedule:
		cycle = earliest // entry
		if entry * cycle < earliest:
			cycle += 1
		if (cycle*entry) - earliest < fastest:
			fastest = (cycle*entry) - earliest
			fast_id = entry
	print(fast_id * fastest)

	# Part 2 Solution
	schedule = []
	with open("day13_input", 'r') as infile:
		earliest = int(infile.readline())
		entries = infile.readline().split(",")
		for pos, entry in enumerate(entries):
			entry = entry.strip()
			if entry != '' and entry != 'x':
				if pos == 0:
					schedule.append((0,int(entry)))
				else:
					schedule.append((pos, int(entry)))
	M_subs = []
	Y_subs = []
	M = 1
	total = 0
	for item in schedule:
		M *= item[1]
	
	for item in schedule:
		M_subs.append(M // item[1])
	
	for i, item in enumerate(schedule):
		t = M_subs[i] % item[1]
		y = None
		for z in range(item[1]):
			if i == 0 and ((z*t) % item[1] == 1):
				y = z
				break
			elif (z*t) % item[1] == item[1]-1:
				y = z
				break
		Y_subs.append(y)
	for i, item in enumerate(schedule):
		total += item[0]*M_subs[i]*Y_subs[i]
	print(total%M)


