#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	start = [16,12,1,0,15,7,11]
	
	while len(start) < 2020:
		if start[-1] not in start[:-1]:
			start.append(0)
		else:
			dist = start[::-1][1:].index(start[-1]) + 1
			start.append(dist)
	print(start[-1])
	
	# Part 2 Solution
	start = [16,12,1,0,15,7,11]
	seen = set()
	last = None
	count = 0
	nums = dict()

	while len(start) > 1:
		current = start.pop(0)
		nums[current] = count
		seen.add(current)
		count += 1
		last = current

	last = start.pop(0)
	while count < 30000000-1:
		if last not in seen:
			seen.add(last)
			nums[last] = count
			last = 0
		else:
			next = count - nums[last]
			nums[last] = count
			last = next
		count += 1
	print(last)
