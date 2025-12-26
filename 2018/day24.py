#!/usr/bin/python


damages = {	'radiation'	: 1,
			'bludgeoning' : 2,
			'slashing' : 3,
			'fire' : 4,
			'cold' : 5}

max_initiative = None

class Group:

	def __init__(self, N, hp, damage, attack_type, initiative, immune, weak):
		global max_initiative
		self.num_units = N
		self.hp = hp
		self.damage_dealt = damage
		self.damage = damages[attack_type]
		self.weak = [ damages[i] for i in weak ]
		self.initiative = initiative
		self.immune = [ damages[i] for i in immune ]
		self.target = None
		self.active = True
		max_initiative = max(max_initiative, self.initiative)

	def takeDamage(self, points):
		self.num_units -= (points / self.hp)
		if self.num_units <= 0:
			self.num_units = 0 
			self.active = False

	def getEffectivePower(self):
		return self.num_units * self.damage_dealt

	def getInitiative(self):
		return self.initiative

	def damageEstimate(self, opponent):
		if not opponent.active:
			return 0
		base = self.getEffectivePower()
		if self.damage in opponent.immune:
			return 0
		if self.damage in opponent.weak:
			return 2 * base
		return base

	def attack(self, opponent):
		if self.active:
			#print self.damageEstimate(opponent), min(self.damageEstimate(opponent) / opponent.hp, opponent.num_units)
			opponent.takeDamage(self.damageEstimate(opponent))		

class Army:

	def __init__(self):
		self.groups = []

	def unitCount(self):
		return sum( x.num_units for x in self.groups )

	def battleOrder(self):
		# sort by Effective Power, ties broken by Initiative
		self.groups = sorted(self.groups, key = lambda x : (x.getEffectivePower(), max_initiative - x.getInitiative()), reverse=True)

	def targetSelect(self, opponentArmy):
		availTargets = []
		for i, group in enumerate(opponentArmy.groups):
			if group.active:
				availTargets.append(i)
		for group in self.groups:
			group.target = None
			high = (0, 0, -1)
			highidx = None
			for idx in availTargets:
				damage = group.damageEstimate(opponentArmy.groups[idx])
				if damage > high[0]:
					high = (damage, opponentArmy.groups[idx].getEffectivePower(), opponentArmy.groups[idx].getInitiative())
					highidx = idx
				elif damage == high[0] and high[0] > 0:
					if opponentArmy.groups[idx].getEffectivePower() > high[1]:
						high = (damage, opponentArmy.groups[idx].getEffectivePower(), opponentArmy.groups[idx].getInitiative())
						highidx = idx
					elif opponentArmy.groups[idx].getEffectivePower() == high[1]:
						if opponentArmy.groups[idx].getInitiative() < high[2]:
							high = (damage, opponentArmy.groups[idx].getEffectivePower(), opponentArmy.groups[idx].getInitiative())
							highidx = idx
			if highidx != None:
				group.target = highidx
				availTargets.remove(highidx)		

	def spawnGroup(self, N, hp, damage, attack_type, initiative, immune, weak):
		self.groups.append(Group(N, hp, damage, attack_type, initiative, immune, weak))

	def printGroups(self):
		for i, group in enumerate(self.groups):
			print "Group", i+1, "contains", group.num_units, "units with", group.hp, "hit points."
			print "  Effective power is: ", group.getEffectivePower(), "Attack type: ", group.damage
			print "  Weak: ", group.weak, "Immune: ", group.immune, "Initiative: ", group.initiative

def parse(line, target_army, boost=0):
	weak_immune = ''
	weak = ''
	immune = ''
	attack = ''
	if "(" in line:
		outer = line[0:line.index("(")-1] + line[line.index(")")+1:]
		inner = line[line.index("(")+1:line.index(")")]
	else:
		inner = ''
		outer = line
	if len(inner) > 0:
		parts = inner.split("; ")
		for part in parts:
			if "weak to " in part:
				part = part.replace("weak to ", '')
				weak = part.split(", ")
			elif "immune to ":
				part = part.replace("immune to ", '')
				immune = part.split(", ")
	outer = outer.split(" ")
	num = int(outer[0])
	hp  = int(outer[4])
	damage  = int(outer[12])+boost
	attack = outer[13]
	initiative = int(outer[-1])

	#print num, hp, damage, attack, initiative, weak, immune
	target_army.spawnGroup(num, hp, damage, attack, initiative, immune, weak)	
	

if __name__ == "__main__":

	# Part 1 Solution

	armies = []

	with open('day24_input', 'r') as infile:
		for line in infile.readlines():
			if ':' in line:
				current_army = Army()
			elif len(line.strip()) == 0:
				armies.append(current_army)
			else:
				parse(line.strip(), current_army)
		armies.append(current_army)

	endgame = False

	while not endgame:

		#for army in armies:
		#	army.printGroups()

		endgame = False
		for army in armies:
			if army.unitCount() == 0:
				endgame = True
				break
		if endgame:
			break

		# Target Selection

		armies[0].battleOrder()
		armies[1].battleOrder()
		armies[0].targetSelect(armies[1])
		armies[1].targetSelect(armies[0])

		# Attack Stage

		attack_order = []
		for i, group in enumerate(armies[0].groups):
			if group.active:
				attack_order.append( (group.getInitiative(), 1, i+1, group.target) )
		for i, group in enumerate(armies[1].groups):
			if group.active:
				attack_order.append( (group.getInitiative(), 2, i+1, group.target) )
		
		attack_order.sort(reverse=True)
		#print attack_order
		for entry in attack_order:
			initiative, army_idx, group_idx, targetID = entry
			if targetID != None:
				armies[army_idx-1].groups[group_idx-1].attack(armies[(army_idx%2)].groups[targetID])

	print armies[0].unitCount() + armies[1].unitCount()

	# Part 2 Solution
	# 3959 too high

	global_boost = -1
	enemywon  = True
	
	while enemywon:

		round_boost = global_boost + 1
		global_boost += 1

		armies = []

		#print "Round Boost: ", round_boost

		with open('day24_input', 'r') as infile:
			for line in infile.readlines():
				if ':' in line:
					current_army = Army()
				elif len(line.strip()) == 0:
					armies.append(current_army)
					round_boost = 0
				else:
					parse(line.strip(), current_army, round_boost)
			armies.append(current_army)

		endgame = False

		while not endgame:

			#for army in armies:
			#	army.printGroups()

			endgame = False
			for army in armies:
				if army.unitCount() == 0:
					endgame = True
					break
			if endgame:
				break

			# Stalemate detection
			start_units = (armies[0].unitCount() + armies[1].unitCount())

			# Target Selection

			armies[0].battleOrder()
			armies[1].battleOrder()
			armies[0].targetSelect(armies[1])
			armies[1].targetSelect(armies[0])

			# Attack Stage

			attack_order = []
			for i, group in enumerate(armies[0].groups):
				if group.active:
					attack_order.append( (group.getInitiative(), 1, i+1, group.target) )
			for i, group in enumerate(armies[1].groups):
				if group.active:
					attack_order.append( (group.getInitiative(), 2, i+1, group.target) )
			
			attack_order.sort(reverse=True)
			#print attack_order
			for entry in attack_order:
				initiative, army_idx, group_idx, targetID = entry
				if targetID != None:
					armies[army_idx-1].groups[group_idx-1].attack(armies[(army_idx%2)].groups[targetID])

			if start_units == (armies[0].unitCount() + armies[1].unitCount()):
				endgame = True

		if (armies[1].unitCount() > 0):
			enemywon = True
		else:
			enemywon = False

	print armies[0].unitCount()

	
	

	
				
				

	
	
