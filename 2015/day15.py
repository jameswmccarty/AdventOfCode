#!/usr/bin/python

import itertools


# algorithm for generating interger partitions of fixed size k
# generator function
def partition_k(n, k):
	if n <= 1:
		return 
	if k <= 0:
		return 
	part = [0] * k
	part[0] = (n-k) + 1
	for i in range(1,k):
		part[i] = 1
	yield part
	yielded = True
	while yielded:
		yielded = False
		for i in range(k):
			if part[i] < part[0]-1:
				yielded = True
				for j in range(1,i+1):
					part[j] = part[i]+1
				part[0] = n - sum(part[1:])
				yield part
				break

class Ingredient:

	def __init__(self, capacity, durability, flavor, texture, calories):
		self.traits = [capacity, durability, flavor, texture, calories]
		
def score_cookie(ingredients, measures):
	sub_scores = [0] * 4
	for i in range(4):
		for idx, amount in enumerate(measures):
			sub_scores[i] += amount * ingredients[idx].traits[i]
	sub_scores = [ max(x,0) for x in sub_scores ]
	return reduce(lambda x, y: x*y, sub_scores)
	
def score_cookie_cal(ingredients, measures):
	sub_scores = [0] * 5
	for i in range(5):
		for idx, amount in enumerate(measures):
			sub_scores[i] += amount * ingredients[idx].traits[i]
	sub_scores = [ max(x,0) for x in sub_scores ]
	if sub_scores[4] != 500:
		return 0
	else:
		sub_scores[4] = 1
	return reduce(lambda x, y: x*y, sub_scores)	
		
if __name__ == "__main__":

	ingredients = []
	# Part 1 Solution
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			ingredients.append(Ingredient(int(line[2].strip(",")), int(line[4].strip(",")), int(line[6].strip(",")), int(line[8].strip(",")), int(line[10].strip())))

	highest_score = 0
	for x in partition_k(100,len(ingredients)):
		for y in itertools.permutations(x):
			highest_score = max(highest_score, score_cookie(ingredients, y))
	print highest_score
	
	# Part 2 Solution
	highest_score = 0
	for x in partition_k(100,len(ingredients)):
		for y in itertools.permutations(x):
			highest_score = max(highest_score, score_cookie_cal(ingredients, y))
	print highest_score
