#!/usr/bin/python

# Advent of Code 2024 Day 09

def checksum(disk):
	total = 0
	for i in range(len(disk)):
		if disk[i] != None:
			total += disk[i]*i
	return total

if __name__ == "__main__":

	# Part 1 Solution
	disk = []
	file_id = 0
	with open("day09_input", "r") as infile:
		disk_map = infile.read().strip() + '0'
		#disk_map = '2333133121414131402' + '0'
	while disk_map:
		file_size, space_size = disk_map[0:2]
		disk += [file_id] * int(file_size)
		disk += [None] * int(space_size)
		disk_map = disk_map[2:]
		file_id += 1

	disk_end = len(disk)-1
	for i in range(len(disk)):
		if i < disk_end and disk[i] == None:
			for j in range(disk_end, i, -1):
				disk_end -= 1
				if disk[j] != None:
					temp = disk[j]
					disk[j] = None
					disk[i] = temp
					break

	print(checksum(disk))

	# Part 2 Solution
	disk = []
	file_id = 0
	seen_file_ids = set()
	with open("day09_input", "r") as infile:
		disk_map = infile.read().strip() + '0'
		#disk_map = '2333133121414131402' + '0'
	while disk_map:
		file_size, space_size = disk_map[0:2]
		disk.append((file_id, int(file_size)))
		disk.append((None, int(space_size)))
		disk_map = disk_map[2:]
		file_id += 1
	last_file_index = len(disk) - 1
	while len(seen_file_ids) != file_id-1:
		for i in range(last_file_index, 0, -1):
			if disk[i][0] != None and disk[i][0] not in seen_file_ids:
				last_file_index = i
				seen_file_ids.add(disk[i][0])
				for j in range(0, i):
					if disk[j][0] == None and disk[j][1] >= disk[i][1]:
						moving_file = disk[i]
						disk[i] = (None, moving_file[1])
						remaining_space = disk[j][1] - moving_file[1]
						disk[j] = (None, remaining_space)
						disk.insert(j, moving_file)
						seen_file_ids.add(moving_file[0])
						break
	built_disk = []
	for value, size in disk:
		built_disk += [value] * size
	print(checksum(built_disk))

