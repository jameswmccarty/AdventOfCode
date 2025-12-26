#!/usr/bin/python


# return True if Player 1 wins
def play_game(deck1, deck2):

	seen = set()
	
	while len(deck1) != 0 and len(deck2) != 0:
	
		if hash(''.join( str(x) for x in deck1+['-']+deck2)) in seen:
			return (True, sum( [ (len(deck1)-i)*x for i,x in enumerate(deck1) ] ))
		seen.add(hash(''.join( str(x) for x in deck1+['-']+deck2)))

		first  = deck1.pop(0)
		second = deck2.pop(0)

		if first <= len(deck1) and second <= len(deck2):
			round_result = play_game(deck1[0:first], deck2[0:second])[0]
			if round_result:
				deck1.append(first)
				deck1.append(second)
			else:
				deck2.append(second)
				deck2.append(first)
		elif first > second:
			deck1.append(first)
			deck1.append(second)
		else:
			deck2.append(second)
			deck2.append(first)

	if len(deck1) == 0:
		return (False, sum( [ (len(deck2)-i)*x for i,x in enumerate(deck2) ] ))
	return (True, sum( [ (len(deck1)-i)*x for i,x in enumerate(deck1) ] ))


if __name__ == "__main__":

	# Part 1 Solution

	deck1 = []
	deck2 = []

	finished_one = False
	with open("day22_input", 'r') as infile:
		for line in infile.readlines():
			if "Player 2" in line:
				finished_one = True
			elif "Player" not in line and line.strip() != '':
				if not finished_one:
					deck1.append(int(line.strip()))
				else:
					deck2.append(int(line.strip()))
	
	while len(deck1) != 0 and len(deck2) != 0:
		first  = deck1.pop(0)
		second = deck2.pop(0)
		if first > second:
			deck1.append(first)
			deck1.append(second)
		else:
			deck2.append(second)
			deck2.append(first)
	
	if len(deck1) == 0:
		print(sum( [ (len(deck2)-i)*x for i,x in enumerate(deck2) ] ) )
	else:
		print(sum( [ (len(deck1)-i)*x for i,x in enumerate(deck1) ] ) )
	
	
	# Part 2 Solution
	deck1 = []
	deck2 = []

	finished_one = False
	with open("day22_input", 'r') as infile:
		for line in infile.readlines():
			if "Player 2" in line:
				finished_one = True
			elif "Player" not in line and line.strip() != '':
				if not finished_one:
					deck1.append(int(line.strip()))
				else:
					deck2.append(int(line.strip()))
	
	print(play_game(deck1, deck2)[1])
