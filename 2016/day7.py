#!/usr/bin/python


def breakout(line):
	inners = []
	outers = []
	segment = ''
	idx = 0
	while idx < len(line):
		if line[idx] == '[':
			outers.append(segment)
			segment = ''
			while line[idx] != ']':
				idx += 1
				segment += line[idx]
			inners.append(segment)
			segment = ''
		else:
			segment += line[idx]
		idx += 1
	outers.append(segment)
	return outers, inners
	
def eval_isp(line):
	inner_support = False
	outer_support = False
	segment = ''
	idx = 0
	while idx < len(line):
		if line[idx] == '[':
			outer_support |= supports_tls(segment)
			segment = ''
			while line[idx] != ']':
				idx += 1
				segment += line[idx]
			inner_support |= supports_tls(segment)
			segment = ''
		else:
			segment += line[idx]
		idx += 1
	outer_support |= supports_tls(segment)
	return outer_support and not inner_support

def supports_tls(line):
	idx = 0
	while idx < len(line)-3:
		if line[idx] == line[idx+3] and line[idx+1] == line[idx+2] and line[idx] != line[idx+1]:
			return True
		idx += 1
	return False
	
def supports_ssl(inpt):
	outers, inners = inpt
	for line in outers:
		idx = 0
		while idx < len(line) - 2:
			aba = line[idx:idx+3]
			if aba[0] == aba[2] and aba[0] != aba[1]:
				bab = aba[1]+aba[0]+aba[1]
				for inline in inners:
					if bab in inline:
						return True
			idx += 1
	return False

if __name__ == "__main__":

	# Part 1 and 2 Solution
	tls_count = 0
	ssl_count = 0
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			if eval_isp(line.strip()):
				tls_count += 1
			if supports_ssl(breakout(line.strip())):
				ssl_count += 1
	print tls_count
	print ssl_count
	
	
			
			
