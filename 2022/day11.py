#!/usr/bin/python

class monkey:

	def __init__(self):
		self.index = None
		self.items = []
		self.inspected_total = 0
		self.op   = None
		self.test = None
		self.true_idx = None
		self.false_idx = None

	def do_inspections(self):
		global monkeys
		while len(self.items) > 0:
			current = self.items.pop(0)
			self.inspected_total += 1
			if 'old * old' in self.op:
				current *= current
			elif '*' in self.op:
				throw,factor = self.op.split(' * ')
				current *= int(factor)
			elif '+' in self.op:
				throw,factor = self.op.split(' + ')
				current += int(factor)
			current //= 3
			if current % self.test == 0:
				monkeys[self.true_idx].items.append(current)
			else:
				monkeys[self.false_idx].items.append(current)

	def do_inspections2(self,modulus):
		global monkeys
		while len(self.items) > 0:
			current = self.items.pop(0)
			self.inspected_total += 1
			if 'old * old' in self.op:
				current *= current
			elif '*' in self.op:
				throw,factor = self.op.split(' * ')
				current *= int(factor)
			elif '+' in self.op:
				throw,factor = self.op.split(' + ')
				current += int(factor)
			current %= modulus
			if current % self.test == 0:
				monkeys[self.true_idx].items.append(current)
			else:
				monkeys[self.false_idx].items.append(current)

	def print(self):
		print("Monkey",self.index,":",self.items)

monkeys = []

if __name__ == "__main__":

	def parse_monkey(block):
		global monkeys
		for line in block:
			line = line.strip()
			if "Monkey" in line:
				throw,m_idx = line.split(' ')
				monkeys += [monkey()]
				monkeys[-1].index = int(m_idx.strip(':'))
			elif "Starting" in line:
				throw,items = line.split(': ')
				items = items.split(', ')
				for entry in items:
					monkeys[-1].items.append(int(entry))
			elif "Test" in line:
				line = line.split(' ')
				monkeys[-1].test = int(line[-1])
			elif "Operation" in line:
				throw,op = line.split(' = ')
				monkeys[-1].op = op
			elif "true:" in line:
				throw,m_idx = line.split(' monkey ')
				monkeys[-1].true_idx = int(m_idx)
			elif "false:" in line:
				throw,m_idx = line.split(' monkey ')
				monkeys[-1].false_idx = int(m_idx)

	# Part 1 Solution
	with open("day11_input","r") as infile:
		inputs = infile.read().strip().split('\n\n')
		for block in inputs:
			block = block.split('\n')
			parse_monkey(block)

	for _ in range(20):
		for m in monkeys:
			m.do_inspections()
		#print("Round",_+1)
		#for m in monkeys:
		#	m.print()

	activity = sorted([m.inspected_total for m in monkeys],reverse=True)
	print(activity[0]*activity[1])

	# Part 2 Solution
	monkeys = []
	with open("day11_input","r") as infile:
		inputs = infile.read().strip().split('\n\n')
		for block in inputs:
			block = block.split('\n')
			parse_monkey(block)

	modulus = 1
	for m in monkeys:
		modulus *= m.test

	for _ in range(10000):
		for m in monkeys:
			m.do_inspections2(modulus)

	activity = sorted([m.inspected_total for m in monkeys],reverse=True)
	print(activity[0]*activity[1])
