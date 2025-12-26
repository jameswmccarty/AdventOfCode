#!/usr/bin/python


tape = {}
pos = 0
state = "A"

states = {
	# State : [ if 0 [ write , movement, next state ],
	#           if 1 [ write , movement, next_state ] ]
	# Movement is 1 for right, -1 for left
			
	"A" : [ [1, 1,"B"], [0, 1,"F"] ],
	"B" : [ [0,-1,"B"], [1,-1,"C"] ],
	"C" : [ [1,-1,"D"], [0, 1,"C"] ],
	"D" : [ [1,-1,"E"], [1, 1,"A"] ],
	"E" : [ [1,-1,"F"], [0,-1,"D"] ],
	"F" : [ [1, 1,"A"], [0,-1,"E"] ]}

def diag_check():
	return sum(tape.values())

if __name__ == "__main__":
	
	# Part 1 Solution
	
	for _ in range(12964419):
		if pos in tape:
			write, move, next = states[state][tape[pos]]
		else:
			write, move, next = states[state][0]
		tape[pos] = write
		pos += move
		state = next

	print diag_check()
