#!/usr/bin/python

import time
import re


if __name__ == "__main__":
	#Part 1 Solution
	
	log = [] # problem input
	with open("day4_input", "r") as infile:
		for line in infile.readlines():
			log.append(line.strip())
	# Order events by timestamp
	log.sort(key = lambda x : time.mktime(time.strptime("2001-" + x[6:17], "%Y-%m-%d %H:%M")))
	
	slept = None # time guard went to sleep
	guards = {}
	for event in log:
		e_time = time.mktime(time.strptime("2001-" + event[6:17], "%Y-%m-%d %H:%M"))
		if "Guard" in event: # Shift change
			g_id = re.search("\d+", event[18:]).group(0) # Pull numerical ID
		elif "asleep" in event: # Got sleepy
			slept = e_time
		elif "wakes" in event: # Woke up
			if g_id in guards.keys():
				guards[g_id].append((slept, e_time)) # tuple of time went to sleep, and time woke up
			else:
				guards[g_id] = [(slept, e_time)]
				
	totals = []
	for guard in guards.keys():
		slept = 0 #total time slept by each guard
		for event in guards[guard]:
			slept += (event[1] - event[0])/60 # convert to mins
		print "Guard " + str(guard) + " slept for " + str(slept) + " mins."
		totals.append((guard, slept))
	
	totals.sort(key = lambda x : x[1], reverse = True) # sort by sleep time
	sleepy_id = totals[0][0] # find most sleepy guard
	print "Most sleepy guard " + str(sleepy_id)
	
	mins = [0] * 60
	for event in guards[sleepy_id]: # review log for sleepy guard
		for i in range(time.gmtime(int(event[0]))[4], time.gmtime(int(event[1]))[4]): #minute to minute
			mins[i] += 1	
	print mins.index(max(mins)) * int(sleepy_id) #minute most spent asleep multiplied by guard id
	
	#Part 2 Solution
	mins_slept = [] #(Guard ID, Max Mins, Minute Most Slept)
	for guard in guards.keys():
		mins = [0] * 60
		for event in guards[guard]:
			for i in range(time.gmtime(int(event[0]))[4], time.gmtime(int(event[1]))[4]): #minute to minute
				mins[i] += 1
		mins_slept.append((guard, max(mins), mins.index(max(mins))))
	
	mins_slept.sort(key = lambda x : x[1], reverse = True)
	print int(mins_slept[0][0]) * mins_slept[0][2]	

	
	"""
	Unused code from playing with sets below.
	"""
	
	#days = {}
	#for event in guards[sleepy_id]: # review log for sleepy guard
	#	day = str(time.gmtime(int(event[0]))[1]) + " " + str(time.gmtime(int(event[0]))[2]) #mon and day
	#	for i in range(time.gmtime(int(event[0]))[4], time.gmtime(int(event[1]))[4]):
	#		if day in days.keys():
	#			days[day].add(i)
	#		else:
	#			days[day] = set()
	#			days[day].add(i)
			
	#firstset = days.values()[0]
	#print days
	#for day in days.values():
	#	print day
	#	firstset = firstset.intersection(day)
	#print firstset.pop() * int(sleepy_id)
	#print firstset
