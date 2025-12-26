#!/usr/bin/python


if __name__ == "__main__":

	on = set()
	
	# brute force attempt to get part 1
	def process1(line):
		global on
		command,ranges = line.split(" ")
		xran,yran,zran = ranges.split(",")
		x1,x2 = xran[2:].split("..")
		y1,y2 = yran[2:].split("..")
		z1,z2 = zran[2:].split("..")

		xmin = max(-50,min(int(x1),int(x2)))
		xmax = min(50,max(int(x1),int(x2)))+1
		ymin = max(-50,min(int(y1),int(y2)))
		ymax = min(50,max(int(y1),int(y2)))+1
		zmin = max(-50,min(int(z1),int(z2)))
		zmax = min(50,max(int(z1),int(z2)))+1
		
		
		if 'on' in command:
			for x in range(xmin,xmax):
				for y in range(ymin,ymax):
					for z in range(zmin,zmax):
						on.add((x,y,z))
		elif 'off' in command:
			for x in range(xmin,xmax):
				for y in range(ymin,ymax):
					for z in range(zmin,zmax):
						on.discard((x,y,z))


	# Part 1 Solution
	
	with open("day22_input","r") as infile:
		for line in infile.readlines():
			process1(line.strip())
	print(len(on))
	
	# Part 2 Solution

	regions = []
	xs = []
	ys = []
	zs = []

	with open("day22_input", "r") as infile:
		for line in infile.readlines():
			command,ranges = line.split(" ")
			xran,yran,zran = ranges.split(",")
			x1,x2 = xran[2:].split("..")
			y1,y2 = yran[2:].split("..")
			z1,z2 = zran[2:].split("..")
			regions.append((command, (int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2))))
			xs.append(int(x1))
			xs.append(int(x2)+1)
			ys.append(int(y1))
			ys.append(int(y2)+1)
			zs.append(int(z1))
			zs.append(int(z2)+1)

	regions = regions[::-1]
	xs.sort()
	ys.sort()
	zs.sort()

	count = 0

	for i in range(len(xs)-1):
		x_filter = [region for region in regions if region[1][0] <= xs[i] <= region[1][1]]
		for j in range(len(ys)-1):
			y_filter = [region for region in x_filter if region[2][0] <= ys[j] <= region[2][1]]
			for k in range(len(zs)-1):
				z_filter = [region for region in y_filter if region[3][0] <= zs[k] <= region[3][1]]
				if len(z_filter) > 0 and z_filter[0][0] == "on":
					count += (xs[i+1]-xs[i]) * (ys[j+1]-ys[j]) * (zs[k+1]-zs[k])
	print(count)

