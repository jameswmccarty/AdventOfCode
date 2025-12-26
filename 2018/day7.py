#!/usr/bin/python


class Node:
	
	def __init__(self, name):
		self.name = name
		self.prerequisites = set()
		self.starttime = None
		self.complete = False
		self.elapsed = 0
		
	def add_prereq(self, requirement):
		self.prerequisites.add(requirement)
	
	def task_time(self):
		# ascii 'A' is decimal 65
		# one minute + character time
		return 60 + ord(self.name) - 64
		
	def start(self, time):
		self.starttime = time

	def tick(self):
		self.elapsed += 1
		if self.elapsed >= self.task_time():
			self.complete = True
	
def parse_node(line):
	line = line.replace("Step ", '')
	line = line.replace("must be finished before step ", '')
	line = line.replace(" can begin.", '')
	parent, child = line.split(" ")
	parent = parent.strip()
	child = child.strip()
	return (parent, child)

if __name__ == "__main__":

	#Part 1 Solution
	
	all_step_names = set()
	deps = []
	all_steps = []	
	
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			p, c = parse_node(line.strip())
			# find set of all steps to complete
			all_step_names.add(p)
			all_step_names.add(c)
			# all prerequisite relationships
			deps.append((p, c))
	
	while len(all_step_names) != 0:
		all_steps.append(Node(all_step_names.pop()))
	
	# map all prerequisite dependancies to step names
	for dep in deps:
		for step in all_steps:
			if step.name == dep[1]:
				step.prerequisites.add(dep[0])
	
	# place in alphabetical order
	all_steps.sort(key = lambda x : x.name)
	
	seq = ''
	while len(all_steps) != 0:
		rmv = None
		for step in all_steps:
			# find job available to start (in alphabetical order)
			if len(step.prerequisites) == 0:
				seq += step.name
				rmv = step
				break
		for step in all_steps:
			# prerequisites now met for job completed
			if rmv.name in step.prerequisites:
				step.prerequisites.remove(rmv.name)
		# remove step from listing
		all_steps.remove(rmv)
		
	print seq
	
	# Part 2 Solution
	
	all_step_names = set()
	deps = []
	all_steps = []	
	
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			p, c = parse_node(line.strip())
			# find set of all steps to complete
			all_step_names.add(p)
			all_step_names.add(c)
			# all prerequisite relationships
			deps.append((p, c))
	
	while len(all_step_names) != 0:
		all_steps.append(Node(all_step_names.pop()))
	
	# map all prerequisite dependancies to step names
	for dep in deps:
		for step in all_steps:
			if step.name == dep[1]:
				step.prerequisites.add(dep[0])
	
	# place in alphabetical order
	all_steps.sort(key = lambda x : x.name)
	
	wall_time = 0
	in_work = [None] * 5 # 5 concurrent jobs max
	while len(all_steps) != 0:
		for i in range(len(in_work)):
			if in_work[i] != None: # job in progress
				if in_work[i].complete:
					# print "Finished " + in_work[i].name
					# job is done, so prerequisites are satisified
					for step in all_steps:
						if in_work[i].name in step.prerequisites:
							step.prerequisites.remove(in_work[i].name)
					# remove job from work queue
					all_steps.remove(in_work[i])
					in_work[i] = None # worker is now available

		for step in all_steps:
			# job can be started
			if len(step.prerequisites) == 0 and step.starttime == None:
				for i in range(len(in_work)):
					# available worker starts the task
					if in_work[i] == None:
						in_work[i] = step
						in_work[i].start(wall_time)
						break
						
		# time pases on all jobs
		for job in in_work:
			if job != None:
				job.tick()
		wall_time += 1
		
	print wall_time-1
	
	
	
