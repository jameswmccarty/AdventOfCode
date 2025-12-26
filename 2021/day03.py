#!/usr/bin/python



if __name__ == "__main__":


	# Part 1 Solution
	with open("day03_input","r") as infile:
		nums = infile.read().strip().split('\n')
	size = len(nums[0])
	mask = int('1'*size,2)
	gamma = 0
	for i in range(size):
		count = 0
		for num in nums:
			if num[i] == '0':
				count -= 1
			else:
				count += 1
		if count > 0:
			gamma |= 1 << (size-1-i)
	print(gamma * (~gamma & mask))

	# Part 2 Solution
	o2_rates = nums[:]
	o2_rate = None
	for i in range(size):
		count = 0
		for num in o2_rates:
			if num[i] == '1':
				count += 1
			else:
				count -= 1
		if count >= 0:
			o2_rates = [ val for val in o2_rates if val[i] == '1' ]
		else:
			o2_rates = [ val for val in o2_rates if val[i] == '0' ]
		if len(o2_rates) == 1:
			o2_rate = int(o2_rates[0],2)
			break

	co2_rates = nums[:]
	co2_rate = None
	for i in range(size):
		count = 0
		for num in co2_rates:
			if num[i] == '1':
				count += 1
			else:
				count -= 1
		if count >= 0:
			co2_rates = [ val for val in co2_rates if val[i] == '0' ]
		else:
			co2_rates = [ val for val in co2_rates if val[i] == '1' ]
		if len(co2_rates) == 1:
			co2_rate = int(co2_rates[0],2)
			break
	print(o2_rate*co2_rate)
