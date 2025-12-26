#!/usr/bin/python

# rotate right by index per rules
def rotr(password, key):
	steps = password.index(key)
	if steps >= 4:
		steps += 1
	steps += 1
	steps %= len(password)
	steps = len(password) - steps
	return password[steps:] + password[0:steps]

def parse(line, password):
	new_password = list(password)
	if 'swap' in line:
		line = line.split(" ")
		x = line[2]
		y = line[5]
		if 'position' in line:
			x = int(x)
			y = int(y)
			new_password[y] = password[x]
			new_password[x] = password[y]
			return ''.join(new_password)
		elif 'letter' in line:
			new_password = password.replace(x,'.')
			new_password = new_password.replace(y,x)
			new_password = new_password.replace('.',y)
			return new_password
	elif 'rotate' in line:
		if 'left' in line or 'right' in line:
			line = line.split(" ")
			steps = int(line[-2]) % len(password)
			if 'right' in line:
				steps = len(password) - steps
			return password[steps:] + password[0:steps]
		elif 'position' in line:
			key = line[-1]
			return rotr(password, key)
			#steps = password.index(key)
			#if steps >= 4:
			#	steps += 1
			#steps += 1
			#steps %= len(password)
			#steps = len(password) - steps
			#return password[steps:] + password[0:steps]
	elif 'reverse' in line:
		line = line.split(' ')
		x = int(line[2])
		y = int(line[4])+1
		y = min(y,len(password))
		substr = password[x:y]
		return password[0:x] + substr[::-1] + password[y:]
	elif 'move' in line:
		line = line.split(' ')
		x = int(line[2])
		y = int(line[5])
		inst_char = password[x]
		new_password = password.replace(inst_char,'')
		new_password = list(new_password)
		new_password.insert(y, inst_char)
		return ''.join(new_password)
	else:
		return None

		
# opposite function
def rev_parse(line, password):
	new_password = list(password)
	if 'swap' in line:
		line = line.split(" ")
		x = line[2]
		y = line[5]
		if 'position' in line:
			x = int(x)
			y = int(y)
			new_password[y] = password[x]
			new_password[x] = password[y]
			return ''.join(new_password)
		elif 'letter' in line:
			new_password = password.replace(x,'.')
			new_password = new_password.replace(y,x)
			new_password = new_password.replace('.',y)
			return new_password
	elif 'rotate' in line:
		if 'left' in line or 'right' in line:
			line = line.split(" ")
			steps = int(line[-2]) % len(password)
			if 'left' in line:
				steps = len(password) - steps
			return password[steps:] + password[0:steps]
		elif 'position' in line:
			key = line[-1]
			new_password = password[1:] + password[0]
			while rotr(new_password, key) != password:
				new_password = new_password[1:] + new_password[0]
			return new_password
			#steps = len(password) - 1 - password.index(key)
			#steps %= len(password)
			#if steps <= 4:
			#	steps += 1
			#steps += 1
			#steps %= len(password)
			#return password[steps:] + password[0:steps]
	elif 'reverse' in line:
		line = line.split(' ')
		x = int(line[2])
		y = int(line[4])+1
		y = min(y,len(password))
		substr = password[x:y]
		return password[0:x] + substr[::-1] + password[y:]
	elif 'move' in line:
		line = line.split(' ')
		x = int(line[2])
		y = int(line[5])
		inst_char = password[y]
		new_password = password.replace(inst_char,'')
		new_password = list(new_password)
		new_password.insert(x, inst_char)
		return ''.join(new_password)
	else:
		return None

		
if __name__ == "__main__":

	# Part 1 Solution
	
	#password = 'abcde'
	password = 'abcdefgh'
	instructions = []
	with open("day21_input", "r") as infile:
		for line in infile.readlines():
			instructions.append(line.strip())
			password = parse(line.strip(), password)
			
	print password
	
	# Part 2 Solution
	password = 'fbgdceah'
	while len(instructions) > 0:
		password = rev_parse(instructions.pop(), password)
	print password

