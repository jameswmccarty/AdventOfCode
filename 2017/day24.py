#!/usr/bin/python


class Component:

	# A component has an A and B port (int values)
	# and the component value is the sum of A+B
	def __init__(self, a, b):
		self.avail = [a,b]
		self.val = a+b

	# A connection can match either end (A or B)
	# and then the connected side is no longer available
	def connects(self, c):
		if c in self.avail:
			return True
		return False

# Return value of the strongest bridge
def max_bridge_val(conn_port, parts):
	strongest = 0
	if len(parts) == 0:
		return 0
	for part in parts:
		if part.connects(conn_port):
			n = part.avail[(part.avail.index(conn_port) + 1) % 2]
			strongest = max(strongest, part.val + max_bridge_val(n, parts.difference({part})))
	return strongest

def l_max(a, b):
	a_len, a_val = a
	b_len, b_val = b
	if a_len !=  b_len:
		if a_len > b_len:
			return a
		else:
			return b
	else:
		if a_val > b_val:
			return a
		else:
			return b
	
# Return the value of the strongest bridge of maximum possible length
def max_long_bridge_val(conn_port, parts):
	longest = (0, 0)
	if len(parts) == 0:
		return 0
	for part in parts:
		if part.connects(conn_port):
			n = part.avail[(part.avail.index(conn_port) + 1) % 2]
			l, v = longest
			nl, nv = max_long_bridge_val(n, parts.difference({part}))
			longest = l_max(longest, (1+nl, part.val+nv))
	return longest		

if __name__ == "__main__":

	parts = set()
	
	# Part 1 Solution

	with open("day24_input", "r") as infile:
		for line in infile.readlines():
			a, b = line.split("/")
			parts.add(Component(int(a.strip()), int(b.strip())))
	print max_bridge_val(0,parts)

	# Part 2 Solution
	
	parts = set()

	with open("day24_input", "r") as infile:
		for line in infile.readlines():
			a, b = line.split("/")
			parts.add(Component(int(a.strip()), int(b.strip())))
	print max_long_bridge_val(0,parts)[1]
