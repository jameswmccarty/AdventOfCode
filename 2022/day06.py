#!/usr/bin/python


if __name__ == "__main__":

	def find_marker(datastream):
		for i in range(len(datastream)-3):
			if len(set(datastream[i:i+4]))==4:
				return i+4

	def find_message(datastream):
		for i in range(len(datastream)-13):
			if len(set(datastream[i:i+14]))==14:
				return i+14

	# Part 1 Solution
	"""
	print(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')) #5
	print(find_marker('nppdvjthqldpwncqszvftbrmjlhg')) #6
	print(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')) #10
	print(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')) #11
	"""
	with open("day06_input","r") as infile:
		print(find_marker(infile.read().strip()))


	# Part 2 Solution
	"""
	print(find_message('mjqjpqmgbljsphdztnvjfqwrcgsmlb')) #19
	print(find_message('bvwbjplbgvbhsrlpgdmjqwftvncz')) #23
	print(find_message('nppdvjthqldpwncqszvftbrmjlhg')) #23
	print(find_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')) #29
	print(find_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')) #26
	"""
	with open("day06_input","r") as infile:
		print(find_message(infile.read().strip()))
