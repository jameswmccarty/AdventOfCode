#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	total = 0
	with open("day06_input", 'r') as infile:
		answers = set()
		for line in infile.readlines():
			if line.strip() == '':
				total += len(answers)
				answers = set()
			else:
				for char in line.strip():
					answers.add(char)
		total += len(answers)
	print(total)

	# Part 2 Solution
	total = 0
	with open("day06_input", 'r') as infile:
		answer_sets = []
		for line in infile.readlines():
			if line.strip() == '':
				start_set = answer_sets.pop(0)
				for next_set in answer_sets:
					start_set.intersection_update(next_set)
				total += len(start_set)
				answer_sets = []
			else:
				line_set = set()
				for char in line.strip():
					line_set.add(char)
				answer_sets.append(line_set)
		start_set = answer_sets.pop(0)
		for next_set in answer_sets:
			start_set.intersection_update(next_set)
		total += len(start_set)
	print(total)
