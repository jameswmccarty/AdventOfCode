#!/usr/bin/python



if __name__ == "__main__":

	adapters = []

	# Part 1 Solution
	with open("day10_input", 'r') as infile:
		for line in infile.readlines():
			adapters.append(int(line))
	adapters.append(max(adapters)+3)
	adapters.append(0)
	adapters.sort()
	ones = 0
	threes = 0
	for i in range(1,len(adapters)):
		if adapters[i]-adapters[i-1] == 1:
			ones += 1
		elif adapters[i]-adapters[i-1] == 3:
			threes += 1
		else:
			print("Invalid chain!")
	print(ones*threes)

	# Part 2 Solution
	
	# Explanation of the method:
	# In example solution, the answer is 19208.
	# Factor tree of 19208 is 2*2*2*7*7*7
	# 
	# The number of available paths from each link
	# in the adapter chain, counting up from (0) to (52) is:
	# 332113321113211211133211111332110
	#
	# Links with only 1 path are represented as 1
	# links with multiple paths out form groups
	# and the total number of paths is the product of these groups
	#
	# Links with multiple paths ordered by a single '2' double the number of solutions
	# Links with a combination '32' yield 4 possible paths
	# Links with a combination '332' yield 7 possible paths
	# 
	# Replacing these strings in the chain produce:
	# 774277
	#
	# The product of these digits is our solution:
	# 7*7*4*2*7 = 19208
	
	path = ""
	for link in adapters:
		paths = 0
		for i in range(1,4):
			if link+i in adapters:
				paths += 1
		path+=str(paths)
	path = path.replace("332","7").replace("32","4").replace("1",'').replace("0",'')
	total = 1
	for digit in path:
		total *= int(digit)
	print(total)
