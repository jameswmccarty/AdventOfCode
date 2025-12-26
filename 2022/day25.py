#!/usr/bin/python

import heapq

def str_to_snafu(digits):
	factors = { '0' : 0, '1' : 1, '2' : 2, '-' : -1, '=' : -2 }
	digits = digits[::-1]
	num = 0
	for place,digit in enumerate(digits):
		num += factors[digit] * (5**place)
	return num

def build_snafu_heap(num,max_len):
	digits = '0-1=2'
	q = []
	heapq.heapify(q)
	heapq.heappush(q,(num,0,'0'*max_len))
	while len(q) > 0:
		val,idx,built = heapq.heappop(q)
		built = list(built)
		for digit in digits:
			built[idx] = digit
			delta = abs(str_to_snafu(''.join(built))-num)
			if delta == 0:
				return ''.join(built)	
			elif delta <= 1.5*num:
				weight = -1/delta
				heapq.heappush(q,(weight,idx+1,''.join(built)))			

if __name__ == "__main__":


	# Part 1 Solution
	with open('day25_input','r') as infile:
		total = sum([ str_to_snafu(line.strip()) for line in infile ])
	log = 0
	while 5**log < total:
		log += 1
	print(build_snafu_heap(total,log).lstrip('0'))
