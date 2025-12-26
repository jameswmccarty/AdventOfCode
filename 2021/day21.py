#!/usr/bin/python


if __name__ == "__main__":

	rolls = 0

	scores = (1,2,3,4,5,6,7,8,9,10)

	def det_dice():
		global rolls
		rolls = 1
		value = 1
		yield value
		while True:
			value += 1
			rolls += 1
			if value == 101:
				value = 1
			yield value
	
	def play(dice,pos):
		roll = sum([next(dice),next(dice),next(dice)]) + pos
		return scores[(roll-1)%10]

	# outcome of rolling 3 quantum dice
	# result / frequency for all 27 rolls
	freqs = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

	def p1_win_states(p1_pos,p2_pos,p1_score,p2_score):
		if p2_score >= 21:
			return 0
		if p1_score >= 21:
			return 1
		p1_wins = 0
		for roll_result_1, num_universes_1 in freqs:
			p1_pos_next = scores[(roll_result_1+p1_pos-1)%10]
			p1_score_next = p1_score + p1_pos_next
			if p1_score_next >= 21:
				p1_wins += num_universes_1
			else:
				for roll_result_2, num_universes_2 in freqs:
					p2_pos_next = scores[(roll_result_2+p2_pos-1)%10]
					p2_score_next = p2_score + p2_pos_next
					p1_wins += num_universes_1 * num_universes_2 * p1_win_states(p1_pos_next,p2_pos_next,p1_score_next,p2_score_next)
		return p1_wins

	def p2_win_states(p1_pos,p2_pos,p1_score,p2_score):
		if p1_score >= 21:
			return 0
		if p2_score >= 21:
			return 1
		p2_wins = 0
		for roll_result_1, num_universes_1 in freqs:
			p1_pos_next = scores[(roll_result_1+p1_pos-1)%10]
			p1_score_next = p1_score + p1_pos_next
			if p1_score_next >= 21:
				p2_wins += 0
			else:
				for roll_result_2, num_universes_2 in freqs:
					p2_pos_next = scores[(roll_result_2+p2_pos-1)%10]
					p2_score_next = p2_score + p2_pos_next
					p2_wins += num_universes_1 * num_universes_2 * p2_win_states(p1_pos_next,p2_pos_next,p1_score_next,p2_score_next)
		return p2_wins

	# Part 1 Solution
	game_dice = det_dice()
	p1_score = 0
	p2_score = 0
	with open("day21_input","r") as infile:
		p1_line = infile.readline()
		p2_line = infile.readline()
	p1_pos = int(p1_line[-2:].strip())
	p2_pos = int(p2_line[-2:].strip())
	while p1_score < 1000 and p2_score < 1000:
		p1_pos = play(game_dice,p1_pos)
		p1_score += p1_pos
		if p1_score >= 1000:
			break
		p2_pos = play(game_dice,p2_pos)
		p2_score += p2_pos
	print(min(p2_score,p1_score)*rolls)
	
	# Part 2 Solution
	with open("day21_input","r") as infile:
		p1_line = infile.readline()
		p2_line = infile.readline()
	p1_pos = int(p1_line[-2:].strip())
	p2_pos = int(p2_line[-2:].strip())
	print(max(p1_win_states(p1_pos,p2_pos,0,0),p2_win_states(p1_pos,p2_pos,0,0)))

