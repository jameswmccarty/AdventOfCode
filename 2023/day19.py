#!/usr/bin/python


ruleset = dict()

def evaluate(part,rule):
	if rule == 'A':
		return True
	if rule == 'R':
		return False
	for criteria in ruleset[rule]:
		if criteria == 'A':
			return True
		if criteria == 'R':
			return False
		if type(criteria) == type(''):
			return evaluate(part,criteria)
		key,op,value,dest = criteria # must be tuple
		if op == 'gt':
			if part[key] > value:
				return evaluate(part,dest)
		if op == 'lt':
			if part[key] < value:
				return evaluate(part,dest)

total = 0
def traverse_count(rule,x,m,a,s):
	global total
	if rule == 'A':
		total += (x[1]+1-x[0])*(m[1]+1-m[0])*(a[1]+1-a[0])*(s[1]+1-s[0])
		return
	if rule == 'R':
		return
	for criteria in ruleset[rule]:
		if criteria == 'A':
			total += (x[1]+1-x[0])*(m[1]+1-m[0])*(a[1]+1-a[0])*(s[1]+1-s[0])
			return
		if type(criteria) == type(''):
			traverse_count(criteria,x,m,a,s)
		if type(criteria) == type(()):
			key,op,value,dest = criteria
			if op == 'gt':
				if key == 'x':
					lo = x[0]
					x = (value+1,x[1])
					traverse_count(dest,x,m,a,s)
					x = (lo,value)
				if key == 'm':
					lo = m[0]
					m = (value+1,m[1])
					traverse_count(dest,x,m,a,s)
					m = (lo,value)
				if key == 'a':
					lo = a[0]
					a = (value+1,a[1])
					traverse_count(dest,x,m,a,s)
					a = (lo,value)
				if key == 's':
					lo = s[0]
					s = (value+1,s[1])
					traverse_count(dest,x,m,a,s)
					s = (lo,value)
			elif op == 'lt':
				if key == 'x':
					hi = x[1]
					x = (x[0],value-1)
					traverse_count(dest,x,m,a,s)
					x = (value,hi)
				if key == 'm':
					hi = m[1]
					m = (m[0],value-1)
					traverse_count(dest,x,m,a,s)
					m = (value,hi)
				if key == 'a':
					hi = a[1]
					a = (a[0],value-1)
					traverse_count(dest,x,m,a,s)
					a = (value,hi)
				if key == 's':
					hi = s[1]
					s = (s[0],value-1)
					traverse_count(dest,x,m,a,s)
					s = (value,hi)

if __name__ == "__main__":


	parts   = []

	# Part 1 Solution
	with open("day19_input", "r") as infile:
		reading_rules = True
		for line in infile:
			if len(line.strip()) == 0:
				reading_rules = False
			elif reading_rules:
				rulename,rules = line.strip().split('{')
				rules = rules[:-1] # shave '}'
				ruleset[rulename] = []
				for entry in rules.split(','):
					if '>' in entry or '<' in entry:
						criteria,dest = entry.split(':')
						if '>' in criteria:
							key,value = criteria.split('>')
							op = 'gt'
						elif '<' in criteria:
							key,value = criteria.split('<')
							op = 'lt'
						ruleset[rulename].append((key,op,int(value),dest))
					else:
						ruleset[rulename].append(entry)
			elif not reading_rules and len(line.strip()) > 0:
				line = line.strip()[1:-1]
				part = dict()
				for entry in line.split(','):
					k,v = entry.split('=')
					part[k]=int(v)
				parts.append(part)

	total = 0
	for part in parts:
		if evaluate(part,'in'):
			total += sum(part.values())
	print(total)


	# Part 2 Solution
	total = 0
	traverse_count('in',(1,4000),(1,4000),(1,4000),(1,4000))
	print(total)

