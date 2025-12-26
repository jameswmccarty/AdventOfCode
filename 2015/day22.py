#!/usr/bin/python


min_spent = float('inf')

def best_duel(me, boss, spells, timer, turn, spent, pt2):

	global min_spent

	me_hp, me_mana = me
	boss_hp, boss_damage = boss

	if pt2 and turn % 2 ==0: # Hard Mode
		me_hp -= 1
	
	# We are dead if out of health.  Stop search if not optimal path.
	if me_hp <= 0 or spent > min_spent:
		return

	# Deal with any active items on entry to function	
	boost_armor  = 0
	for idx in range(len(timer)):
		if timer[idx] > 0: # Spell is active
			boss_hp      -= spells[idx].damage
			me_hp		 += spells[idx].heal
			me_mana      += spells[idx].mana
			boost_armor  += spells[idx].armor

	if boss_hp <= 0: # We won due to applied spells
		min_spent = min(spent, min_spent)
		return
			
	timer = [ max(0,x-1) for x in timer ] # decrement timers for turn
	
	if turn % 2 == 0: # Our Turn
		base_mana = me_mana
		base_hp = me_hp
		base_spent = spent
		# Select a spell to cast.  If you cannot afford to cast a spell, you lose.
		for idx in range(len(spells)):
			me_mana = base_mana # reset for each possible purchase
			me_hp   = base_hp
			spent = base_spent
			if timer[idx] == 0: # spell not active
				if spells[idx].cost <= me_mana: # can afford to cast
					spent += spells[idx].cost
					me_mana -= spells[idx].cost
					round_list = [x for x in timer]
					round_list[idx] = spells[idx].ttl
					best_duel((me_hp, me_mana), (boss_hp, boss_damage), spells, round_list, turn+1, spent, pt2)
	else: # Boss Turn
		me_hp -= max(1,boss_damage-boost_armor)
		round_list = [x for x in timer]
		best_duel((me_hp, me_mana), (boss_hp, boss_damage), spells, round_list, turn+1, spent, pt2)		

class Spell:

	def __init__(self, title, cost, damage, armor, heal, mana, ttl):
		self.title = title
		self.cost = cost
		self.damage = damage
		self.armor = armor
		self.heal = heal
		self.mana = mana
		self.ttl = ttl	
		
if __name__ == "__main__":

	spells = [  Spell("Magic Missile", 53, 4, 0, 0, 0, 1),
				Spell("Drain", 73, 2, 0, 2, 0, 1),
				Spell("Shield", 113, 0, 7, 0, 0, 6),
				Spell("Poison", 173, 3, 0, 0, 0, 6),
				Spell("Recharge", 229, 0, 0, 0, 101, 5) ]
				
	# Part 1 Solution
	best_duel((50,500), (51,9), spells, [0,0,0,0,0], 0, 0, False)
	print min_spent
	
	# Part 2 Solution
	min_spent = float('inf')
	best_duel((50,500), (51,9), spells, [0,0,0,0,0], 0, 0, True)
	print min_spent
	
	
