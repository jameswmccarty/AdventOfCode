#!/usr/bin/python

import itertools


class Player:

	def __init__(self, hp):
		self.armor = 0
		self.hp = hp
		self.damage = 0
		
	def equip(self, weapon, armor, rings):
		self.damage += weapon.damage
		self.armor += armor.armor
		for ring in rings:
			self.damage += ring.damage
			self.armor += ring.armor
			
def win_boss(me):

	boss = Player(100)
	boss.damage = 8
	boss.armor  = 2
	
	while True:
		boss.hp -= max(1, me.damage - boss.armor)
		if boss.hp <= 0:
			return True
		me.hp -= max(1, boss.damage - me.armor)
		if me.hp <= 0:
			return False

class Item:

	def __init__(self, cost, damage, armor):
		self.cost = cost
		self.damage = damage
		self.armor = armor

if __name__ == "__main__":

	weapons = [ Item(8,4,0),
				Item(10,5,0),
				Item(25,6,0),
				Item(40,7,0),
				Item(74,8,0) ]
	
	armor = [	Item(0,0,0), # No armor option
				Item(13,0,1),
				Item(31,0,2),
				Item(53,0,3),
				Item(75,0,4),
				Item(102,0,5) ]
				
	rings = [	Item(0,0,0), # No ring option
				Item(0,0,0),
				Item(25,1,0),
				Item(50,2,0),
				Item(100,3,0),
				Item(20,0,1),
				Item(40,0,2),
				Item(80,0,3) ]
				
	ring_opts = [ x for x in itertools.combinations(rings, 2) ] # 0 - 2 rings can be worn
	
	
	# Part 1 Solution
	
	min_cost = float('inf')
	
	for weapon in weapons:
		for protec in armor:
			for combo in ring_opts:
				me = Player(100)
				me.equip(weapon, protec, combo)
				spent = weapon.cost + protec.cost + combo[0].cost + combo[1].cost
				if win_boss(me):
					min_cost = min(min_cost, spent)
	print min_cost
	
	# Part 2 Solution
	
	max_cost = 0
	
	for weapon in weapons:
		for protec in armor:
			for combo in ring_opts:
				me = Player(100)
				me.equip(weapon, protec, combo)
				spent = weapon.cost + protec.cost + combo[0].cost + combo[1].cost
				if not win_boss(me):
					max_cost = max(max_cost, spent)
	print max_cost
