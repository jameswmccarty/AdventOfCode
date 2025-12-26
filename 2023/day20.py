#!/usr/bin/python


from collections import deque
import math

high_sent = 0
low_sent  = 0

cycle_counters = { 'pv' : 0,
		   'vv' : 0,
		   'mr' : 0,
		   'bl' : 0}
cycle_count = 0

class Button:

	def __init__(self,output):
		self.name = 'button'
		self.output = None

	def get_name(self):
		return self.name

	def add_output(self,module):
		self.output = module

	def kind(self):
		return 'button'

	def tick(self):
		return False

	def press(self):
		global low_sent
		#print(self.get_name(), "Sent a pulse")
		low_sent += 1
		self.output.recv('-low',self)

class Output:

	def __init__(self,a):
		self.name = a
		self.low_count = 0
		self.high_count = 0

	def get_name(self):
		return self.name

	def kind(self):
		return self.name

	def tick(self):
		return False

	def recv(self,pulse,source):
		global low_sent,high_sent
		if pulse == '-low':
			self.low_count += 1
		if pulse == '-high':
			self.high_count += 1
		#print("Outputs are now: ",self.low_count,"-low and",self.high_count,"-high pulses")
		#print("Global counts are",low_sent,high_sent)

class Broadcaster:

	def __init__(self):
		self.name = 'broadcaster'
		self.outputs = []
		self.signal_line = deque()

	def get_name(self):
		return self.name

	def kind(self):
		return 'broadcaster'

	def add_output(self,module):
		self.outputs.append(module)

	def tick(self):
		global low_sent,high_sent
		if self.signal_line:
			pulse = self.signal_line.popleft()
			for e in self.outputs:
				#print(self.get_name(), "Sent a pulse to ",e.get_name())
				e.recv(pulse,self)
				if pulse == '-low':
					low_sent += 1
				else:
					high_sent += 1
			return True
		return False

	def recv(self,pulse,source):
		self.signal_line.append(pulse)

class FlipFlop:

	def __init__(self,name):
		self.name = name[1:]
		self.outputs = []
		self.state = False
		self.signal_line = deque()

	def kind(self):
		return 'flipflop'

	def get_name(self):
		return self.name

	def add_output(self,module):
		self.outputs.append(module)

	def tick(self):
		global low_sent,high_sent
		if self.signal_line:
			pulse = self.signal_line.popleft()
			if pulse == '-low':
				self.state ^= True
				if self.state:
					for e in self.outputs:
						e.recv('-high',self)
						high_sent += 1
				else:
					for e in self.outputs:
						low_sent += 1
						e.recv('-low',self)
			return True
		return False

	def recv(self,pulse,source):
		#print(self.get_name(), "Got a pulse from",source.get_name())
		self.signal_line.append(pulse)

class Conjunction:

	def __init__(self,name):
		self.name = name[1:]
		self.outputs = []
		self.inputs  = dict()
		self.signal_line = deque()

	def get_name(self):
		return self.name

	def kind(self):
		return 'conjunction'

	def add_output(self,module):
		self.outputs.append(module)

	def add_input(self,module):
		self.inputs[module] = '-low'

	def tick(self):
		global low_sent,high_sent,cycle_counters
		if all( value == '-high' for value in self.inputs.values() ):
			if self.get_name() in cycle_counters and cycle_counters[self.get_name()] == 0:
				cycle_counters[self.get_name()] = cycle_count
			for e in self.outputs:
				e.recv('-low',self)
				low_sent += 1
		else:
			for e in self.outputs:
				e.recv('-high',self)
				high_sent += 1
		return False

	def recv(self,pulse,source):
		self.inputs[source] = pulse
		self.tick()

def gen_module_pass1(line):
	source,dest = line.strip().split(' -> ')
	if source == 'button':
		return Button(dest.strip())
	if source == 'broadcaster':
		return Broadcaster()
	if source == 'output':
		return Output()
	if '%' in source:
		return FlipFlop(source)
	if '&' in source:
		return Conjunction(source)
	return None


if __name__ == "__main__":

	Modules = dict()

	# Part 1 Solution
	with open("day20_input", "r") as infile:
		for line in infile:
			module = gen_module_pass1(line)
			Modules[module.get_name()] = module

	#if 'output' not in Modules:
	#	Modules['output'] = Output('output')

	with open("day20_input", "r") as infile:
		for line in infile:
			source,dest = line.strip().split(' -> ')
			for entry in dest.split(', '):
				if entry not in Modules:
					Modules[entry] = Output(entry)
			if source == 'broadcaster':
				for entry in dest.split(', '):
					Modules[source].add_output(Modules[entry])
			if source == 'button':
				for entry in dest.split(', '):
					Modules[source].add_output(Modules[entry])
			if '%' in source:
				for entry in dest.split(', '):
					Modules[source[1:]].add_output(Modules[entry])
			if '&' in source:
				for entry in dest.split(', '):
					Modules[source[1:]].add_output(Modules[entry])
			for entry in dest.split(', '):
				if Modules[entry].kind() == 'conjunction':
					source_name = source[1:] if '%' in source or '&' in source else source
					Modules[entry].add_input(Modules[source_name])

	for _ in range(1000):
		Modules['button'].press()
		while any( v.tick() if v.kind() != 'conjunction' else False for k,v in Modules.items() ):
			continue

	print(low_sent*high_sent)

	# Part 2 Solution
	Modules = dict()
	low_sent = 0
	high_sent = 0

	# Part 1 Solution
	with open("day20_input", "r") as infile:
		for line in infile:
			module = gen_module_pass1(line)
			Modules[module.get_name()] = module

	#if 'output' not in Modules:
	#	Modules['output'] = Output('output')

	with open("day20_input", "r") as infile:
		for line in infile:
			source,dest = line.strip().split(' -> ')
			for entry in dest.split(', '):
				if entry not in Modules:
					Modules[entry] = Output(entry)
			if source == 'broadcaster':
				for entry in dest.split(', '):
					Modules[source].add_output(Modules[entry])
			if source == 'button':
				for entry in dest.split(', '):
					Modules[source].add_output(Modules[entry])
			if '%' in source:
				for entry in dest.split(', '):
					Modules[source[1:]].add_output(Modules[entry])
			if '&' in source:
				for entry in dest.split(', '):
					Modules[source[1:]].add_output(Modules[entry])
			for entry in dest.split(', '):
				if Modules[entry].kind() == 'conjunction':
					source_name = source[1:] if '%' in source or '&' in source else source
					Modules[entry].add_input(Modules[source_name])

	while True:
		cycle_count += 1
		Modules['button'].press()
		while any( v.tick() if v.kind() != 'conjunction' else False for k,v in Modules.items() ):
			continue
		if all( x != 0 for x in cycle_counters.values() ):
			print(math.lcm(*cycle_counters.values()))
			exit()
		
	
