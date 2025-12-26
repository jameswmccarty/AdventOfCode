#!/usr/bin/python

if __name__ == "__main__":

	beacons_sets = []
	beacons_sets_rotated = []
	scanner_posits = dict()

	conv_beacons_to_scanner_idx_map = dict()
	idx_to_scanner_loc_map = dict()

	def rotation_poss_set(x,y,z):
		orientations = list()
		perms = [(x, y, z),(x, z, y),(y, x, z),(y, z, x),(z, x, y),(z, y, x)]
		signs = [(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
		for p in perms:
			for s in signs:
				orientations.append((p[0]*s[0],p[1]*s[1],p[2]*s[2]))
		return orientations
	
	def apply_against(base_set,rotated_candidate_set):
		offset_histogram = dict()
		for e1 in rotated_candidate_set:
			for e2 in base_set:
				dx,dy,dz = e1[0]-e2[0],e1[1]-e2[1],e1[2]-e2[2]
				if (dx,dy,dz) in offset_histogram:
					offset_histogram[(dx,dy,dz)] += 1
					if offset_histogram[(dx,dy,dz)] >= 12:
						return (dx,dy,dz)
				else:
					offset_histogram[(dx,dy,dz)] = 1
		return None

	def mh_dist(a,b):
		return sum([ a[i]-b[i] for i in range(3) ])

	# Part 1 Solution

	with open("day19_input", "r") as infile:
		current_group = []
		for line in infile.readlines():
			if "---" in line:
				current_group = []
			elif line.strip() == '':
				beacons_sets.append(current_group)
				continue
			else:
				x,y,z = line.strip().split(",")
				current_group.append((int(x),int(y),int(z)))
		beacons_sets.append(current_group)
	
	for scan_group in beacons_sets:
		rotated_set = []
		for entry in scan_group:
			rotated_set.append(rotation_poss_set(entry[0],entry[1],entry[2]))
		beacons_sets_rotated.append(rotated_set)

	base_set = beacons_sets[0]
	all_beacons_converted = { _ for _ in base_set }
	unmatched_idxs = [ x for x in range(1,len(beacons_sets)) ]
	idx_to_scanner_loc_map[0] = (0,0,0)

	while len(unmatched_idxs) > 0:
		for entry in unmatched_idxs:
			base_set = list(all_beacons_converted)
			for idx in range(48):
				trial_list = []
				for point in beacons_sets_rotated[entry]:
					trial_list.append(point[idx])
				match_offset = apply_against(base_set,trial_list)
				if match_offset != None:
					unmatched_idxs.remove(entry)
					idx_to_scanner_loc_map[entry] = match_offset
					for old_point in trial_list:
						ox,oy,oz = old_point
						dx,dy,dz = match_offset
						nx,ny,nz = ox-dx,oy-dy,oz-dz
						if (nx,ny,nz) not in all_beacons_converted:
							all_beacons_converted.add((nx,ny,nz))
					break
	print(len(all_beacons_converted))

	# Part 2 Solution

	max_dist = 0
	all_scanner_locs = [ v for k,v in idx_to_scanner_loc_map.items() ]
	for i in range(len(all_scanner_locs)):
		for j in range(i,len(all_scanner_locs)):
			max_dist = max(max_dist,mh_dist(all_scanner_locs[i],all_scanner_locs[j]))
	print(max_dist)

