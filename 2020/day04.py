#!/usr/bin/python


def valid(buf):
	req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	for field in req_fields:
		if field+":" not in buf:
			return 0
	return 1

def valid2(buf):
	req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	nums = [ chr(i) for i in range(48,58) ]
	hexd = [ chr(i) for i in range(97,103) ] + nums
	for field in req_fields:
		if field+":" not in buf:
			return 0
	buf = buf.replace("\n", ' ')
	buf = buf.split(" ")
	buf.remove('')
	if len(buf) != 7 and len(buf) != 8:
		return 0
	
	for entry in buf:
		k, v = entry.split(":")
		if k == "byr":
			if len(v) != 4:
				return 0
			try:
				v = int(v)
			except:
				return 0
			if v < 1920 or v > 2002:
				return 0
		if k == "iyr":
			if len(v) != 4:
				return 0
			try:
				v = int(v)
			except:
				return 0
			if v < 2010 or v > 2020:
				return 0
		if k == "eyr":
			if len(v) != 4:
				return 0
			try:
				v = int(v)
			except:
				return 0
			if v < 2020 or v > 2030:
				return 0
		if k == "hgt":
			if v[-2:] == "cm" and len(v) == 5:
				try:
					hgt = int(v[0:3])
				except:
					return 0
				if hgt < 150 or hgt > 193:
					return 0
			elif v[-2:] == "in" and len(v) == 4:
				try:
					hgt = int(v[0:2])
				except:
					return 0
				if hgt < 59 or hgt > 76:
					return 0
			else:
				return 0
		if k == "hcl":
			if v[0] != '#' or len(v) != 7:
				return 0
			for i in range(1,7):
				if v[i] not in hexd:
					return 0
		if k == "ecl":
			if v not in eyes:
				return 0
		if k == "pid":
			if len(v) != 9:
				return 0
			for char in v:
				if char not in nums:
					return 0
	return 1

if __name__ == "__main__":

	# Part 1 Solution
	
	valids = 0
	with open("day04_input", 'r') as infile:
		buf = ''
		for line in infile.readlines():
			if line.strip() == '':
				valids += valid(buf)
				buf = ''
			else:
				buf += line
		if buf != '':
			valids += valid(buf)
	print(valids)

	# Part 2 Solution
	valids = 0
	with open("day04_input", 'r') as infile:
		buf = ''
		for line in infile.readlines():
			if line.strip() == '':
				valids += valid2(buf)
				buf = ''
			else:
				buf += line
		if buf != '':
			valids += valid2(buf)
	print(valids)

