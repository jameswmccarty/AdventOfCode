#!/usr/bin/python

rules = dict()

def parse(line):
	rule_num, line = line.split(": ")
	if "|" in line:
		line = line.split("|")
	else:
		line = [line]

	if chr(34) in line[0]: # double quote
		 rule = line[0].replace(chr(34),'')
	else:
		rule = []
		for sub in line:
			rule.append(sub.strip().split(" "))

	rules[rule_num] = rule

"""
def resolve_tree(rule_num):
	if rules[rule_num].terminal:
		return rules[rule_num].value
	combos = []
	for branch in rules[rule_num].value:
		local = []
		for b in branch:
			local.append(resolve(b))
		if sum([ 1 for x in local if type(x) == type(list())]) == 0:
			local = ''.join(local)
		combos.append(local)
	return combos
"""

def gen_seq(seq, string):
	if len(seq) == 0:
		yield string
	else:
		next = seq[0]
		seq = seq[1:]
		for result in verify(next, string):
			yield from gen_seq(seq, result)

def expand(branch, string):
	for seq in branch:
		yield from gen_seq(seq, string)

def verify(idx, string):
	if type(rules[idx]) == type(list()):
		yield from expand(rules[idx], string)
	else:
		if len(string) > 0 and string[0] == rules[idx]:
			yield string[1:]

if __name__ == "__main__":

	# Part 1 Solution
	texts = []
	with open("day19_input", 'r') as infile:
		rule_end = False
		for line in infile.readlines():
			if not rule_end:
				if line.strip() == '':
					rule_end = True
				else:
					parse(line.strip())
			else:
				texts.append(line.strip())

	valid = 0
	for text in texts:
		if '' in [ x for x in verify('0', text)]:
			valid += 1
	print(valid)


	# Part 2 Solution
	rules['8'] = [['42'], ['42', '8']]
	rules['11'] = [['42', '31'], ['42', '11', '31']]
	valid = 0
	for text in texts:
		if '' in [ x for x in verify('0', text)]:
			valid += 1
	print(valid)
