#!/usr/bin/python


def parse(seat_id):
	seat_idx = seat_id[7:].replace("R","1").replace("L","0")
	row_idx  = seat_id[0:7].replace("F","0").replace("B","1")
	return int(row_idx,2) * 8 + int(seat_idx,2)

if __name__ == "__main__":

	# Part 1 Solution
	with open("day05_input", 'r') as infile:
		print(max([parse(line) for line in infile.readlines()]))

	# Part 2 Solution
	with open("day05_input", 'r') as infile:
		all_ids = set([parse(line) for line in infile.readlines()])
		front = min(all_ids)
		back  = max(all_ids)
		avail = set([i for i in range(front,back)])
		print(avail.difference(all_ids).pop())

