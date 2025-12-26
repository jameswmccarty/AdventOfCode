#!/usr/bin/python


if __name__ == "__main__":

	from collections import deque

	cave_map = dict()
	total_valids = set()
	
	def is_lower(word):
		return True if word.lower() == word else False

	def cave_bfs_path_count1(start):
		path_count = 0
		q = deque()
		q.append((start,set()))
		while len(q) > 0:
			current,path = q.popleft()
			path.add(current)
			for entry in cave_map[current]:
				if entry == "end":
					path_count += 1
				elif (is_lower(entry) and entry not in path) or (not is_lower(entry)):
					q.append((entry,path.copy()))
		return path_count

	def cave_bfs_path_count2(start,allowed_double):
		global total_valids
		q = deque()
		q.append((start,''))
		while len(q) > 0:
			current,path = q.popleft()
			path += '-'+current
			for entry in cave_map[current]:
				if entry == "end":
					total_valids.add(path)
				elif entry != "start" and (not is_lower(entry) or (entry not in path) or (entry == allowed_double and (path.count(entry) < 2))):
					q.append((entry,path[:]))

	def cave_dfs_path_count2(current,allowed_double,path):
		global total_valids
		if current == "end":
			total_valids.add(path)
			return
		for entry in cave_map[current]:
			if entry != "start" and (not is_lower(entry) or (entry not in path) or (entry == allowed_double and (path.count(entry) < 2))):
				cave_dfs_path_count2(entry,allowed_double,path+"-"+current)

	# Part 1 Solution
	with open("day12_input","r") as infile:
		lines = infile.read().strip().split('\n')
	for line in lines:
		left,right = line.split("-")
		if left not in cave_map:
			cave_map[left] = set()
		cave_map[left].add(right)
		if right not in cave_map:
			cave_map[right] = set()
		cave_map[right].add(left)
	print(cave_bfs_path_count1("start"))

	# Part 2 Solution
	doubles = { x for x in cave_map.keys() if is_lower(x) and len(cave_map[x]) > 3 }
	doubles.discard("end")
	doubles.discard("start")
	for entry in doubles:
		#cave_bfs_path_count2("start",entry)
		cave_dfs_path_count2("start",entry,'')
	print(len(total_valids))

