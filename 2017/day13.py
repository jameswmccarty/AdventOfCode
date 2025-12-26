#!/usr/bin/python



class Scanner:

	def __init__(self, layer, depth):
		self.layer = layer
		self.depth = depth
		self.sev = self.layer * self.depth
		
	def hit(self, t):
		if (t % (2*self.depth-2)) == 0:
			return self.sev
		return 0

	def found(self, t):
		if (t % (2*self.depth-2)) == 0:
			return True
		return False
		
	
if __name__ == "__main__":

    # Part 1 Solution

	scanners = []

	# Part 1 Solution
	
	with open("day13_input", "r") as infile:
		for line in infile.readlines():
			layer, depth = line.split(":")
			scanners.append(Scanner(int(layer.strip()), int(depth.strip())))
	
	severity = 0
	t = 0
	while len(scanners) > 0:
		for scanner in scanners:
			if scanner.layer == t:
				severity += scanner.hit(t)
				scanners.remove(scanner)
		t += 1
	
	print severity

	# Part 2 Solution
	
	scanners = []
	
	max_layer = 0
	
	with open("day13_input", "r") as infile:
		for line in infile.readlines():
			layer, depth = line.split(":")
			scanners.append(Scanner(int(layer.strip()), int(depth.strip())))
			max_layer = max(max_layer, int(layer.strip()))
	
	delay = 0
	while True:				
		detected = False
		t = 0
		for t in range(max_layer+1):
			for scanner in scanners:
				if detected:
					break
				if scanner.layer == t:
					detected |= scanner.found(t+delay)

			t += 1
		
		if not detected:
			print delay
			break
		
		delay += 1
		
		
			
