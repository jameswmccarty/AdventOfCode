#!/usr/bin/python


# Return game number if line was possible or 0 otherwise
def possible_game(line,max_red,max_green,max_blue):
	game,trials = line.strip().split(':')
	for trial in trials.split(';'):
		for entry in trial.split(','):
			if "red" in entry:
				if int(entry.replace(' red','')) > max_red:
					return 0
			elif "green" in entry:
				if int(entry.replace(' green','')) > max_green:
					return 0
			elif "blue" in entry:
				if int(entry.replace(' blue','')) > max_blue:
					return 0
	return int(game.replace('Game ',''))

def game_power(line):
	r,g,b = 0,0,0
	game,trials = line.strip().split(':')
	for trial in trials.split(';'):
		for entry in trial.split(','):
			if "red" in entry:
				r = max(r,int(entry.replace(' red','')))
			elif "green" in entry:
				g = max(g,int(entry.replace(' green','')))
			elif "blue" in entry:
				b = max(b,int(entry.replace(' blue','')))
	return r*g*b

if __name__ == "__main__":

	# Part 1 Solution
	with open("day02_input", "r") as infile:
		print(sum(possible_game(line,12,13,14) for line in infile))

	# Part 2 Solution
	with open("day02_input", "r") as infile:
		print(sum(game_power(line) for line in infile))
