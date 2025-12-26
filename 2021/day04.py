#!/usr/bin/python

if __name__ == "__main__":

	def play_move(board, number):
		return [ (item[0],True) if item[0] == number else item for item in board ]

	def test_board(board):
		for j in range(5):
			if sum([x[1] for x in board[j*5:j*5+5]]) == 5:
				return True
		for j in range(5):
			if sum([ board[j+i][1] for i in [0,5,10,15,20] ]) == 5:
				return True
		return False

	def score_board(board,number):
		total = sum([ x[0] for x in board if not x[1] ])
		return total*number

	# Part 1 Solution
	boards = []
	with open("day04_input","r") as infile:
		moves = [ int(x) for x in infile.readline().strip().split(',') ]
		row_count = 0
		board = []
		for line in infile.readlines():
			if line.strip() == '':
				continue
			else:
				line = line.replace('  ',' ')
				board += [(int(x),False) for x in line.strip().split(' ')]
				row_count += 1
				if row_count == 5:
					boards.append(board)
					board = []
					row_count = 0

	won = False
	for move in moves:
		if won:
			break
		for idx,board in enumerate(boards):
			boards[idx] = play_move(board, move)
			if test_board(boards[idx]):
				print(score_board(boards[idx],move))
				won = True
				break

	# Part 2 Solution
	boards = []
	with open("day04_input","r") as infile:
		moves = [ int(x) for x in infile.readline().strip().split(',') ]
		row_count = 0
		board = []
		for line in infile.readlines():
			if line.strip() == '':
				continue
			else:
				line = line.replace('  ',' ')
				board += [(int(x),False) for x in line.strip().split(' ')]
				row_count += 1
				if row_count == 5:
					boards.append(board)
					board = []
					row_count = 0

	last_score = None
	for move in moves:
		for idx,board in enumerate(boards):
			if board != None:
				boards[idx] = play_move(board, move)
				if test_board(boards[idx]):
					last_score = score_board(boards[idx],move)
					boards[idx] = None
	print(last_score)

