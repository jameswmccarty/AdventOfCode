#!/usr/bin/python

def score(card):
	num,points = card.split(":")
	win,have   = points.split("|")
	win,have  = set(win.strip().split()),set(have.strip().split())
	overlaps = len(win.intersection(have))
	return 0 if overlaps == 0 else 2**(overlaps-1)

if __name__ == "__main__":

	# Part 1 Solution
	with open("day04_input", "r") as infile:
		print(sum(score(line) for line in infile))

	# Part 2 Solution
	won = dict()
	with open("day04_input", "r") as infile:
		for card in infile:
			num,points = card.split(":")
			win,have   = points.split("|")
			win,have  = set(win.strip().split()),set(have.strip().split())
			offset = len(win.intersection(have))
			num = int(num.lstrip("Card "))
			if num not in won:
				won[num] = 1
			if offset != 0:
				for win in range(num+1,num+offset+1):
					if win not in won:
						won[win] = 1+won[num]
					else:
						won[win] += won[num]
	print(sum(won.values()))
