#!/usr/bin/python


outputs = dict() # key = number, value = [ ints ]
bots = dict()

class Bot:

	def __init__(self, identity, lowpass, highpass):
		self.identity = identity
		self.num = int(identity)
		self.lowpass = lowpass # ('bot' | 'output', #) tuple
		self.highpass = highpass # ('bot' | 'output', #) tuple
		self.has = []
		self.had = []
		
	def value_pass(self, input):
		int_input = int(input)
		self.has.append(int_input)
		if len(self.has) >= 2:
			while len(self.has) > 0:
				item1 = self.has.pop()
				item2 = self.has.pop()
				self.had.append(item1)
				self.had.append(item2)
				if self.lowpass[0] == 'bot':
					bots[self.lowpass[1]].value_pass(min(item1, item2))
				else:
					outputs[self.lowpass[1]].append(min(item1, item2))
				if self.highpass[0] == 'bot':
					bots[self.highpass[1]].value_pass(max(item1, item2))
				else:
					outputs[self.highpass[1]].append(max(item1, item2))					
			
		

if __name__ == "__main__":

	# Part 1 Solution
	
	# First pass builds bots with rules
	with open("day10_input", "r") as infile:
		for line in infile.readlines():
			if 'gives' in line: # contains new bot with rules
				line = line.split(" ")
				new_bot = Bot(line[1], (line[5], line[6]), (line[10], line[11].strip()))
				bots[new_bot.identity] = new_bot
				if line[5] == 'output': # pass off to 'output' not 'bot'
					outputs[line[6]] = []
				if line[10] == 'output':
					outputs[line[11].strip()] = []

	# Second pass distributes values to bots
	with open("day10_input", "r") as infile:
		for line in infile.readlines():
			if 'value' in line:
				line = line.split(" ")
				bots[line[5].strip()].value_pass(int(line[1]))
				
	for bot in bots:
		if 61 in bots[bot].had and 17 in bots[bot].had:
			print bot

	# Part 2 Solution
	print outputs['0'][0] * outputs['1'][0] * outputs['2'][0]
