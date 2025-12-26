#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	with open("day08_input","r") as infile:
		digits = [ x for x in infile.read().strip().split('\n') ]
	count = 0
	for segset in digits:
		unknown, known = segset.split(" | ")
		count += sum( [ len(x) in [2,3,4,7] for x in known.split(" ") ] )
	print(count)

	# Part 2 Solution

	digit_map = {'abcefg':'0','cf':'1','acdeg':'2','acdfg':'3','bcdf':'4','abdfg':'5','abdefg':'6','acf':'7','abcdefg':'8','abcdfg':'9'}
	all_sums = 0
	for segset in digits:
		example, unk = segset.split(" | ")
		lens = sorted([x for x in example.split(" ")], key=lambda x:len(x))
		# sorted by length, take sizes 2, 3, 4 and 7
		# correlate to strings representing one, seven, four and eight
		one, seven, four, eight = lens[0], lens[1], lens[2], lens[-1]
		A = seven.replace(one[0],'').replace(one[1],'')
		four = four.replace(one[0],'').replace(one[1],'')
		bd_segs = ((four[0],four[1]),(four[1],four[0]))
		cf_segs = ((one[0],one[1]),(one[1],one[0]))
		eg_segs = eight.replace(A,'').replace(one[0],'').replace(one[1],'').replace(four[0],'').replace(four[1],'')
		eg_segs = ((eg_segs[0],eg_segs[1]),(eg_segs[1],eg_segs[0]))
		for C,F in cf_segs:
			for B,D in bd_segs:
				for E,G in eg_segs:
					trial = example.replace(A,'A').replace(B,'B').replace(C,'C').replace(D,'D').replace(E,'E').replace(F,'F').replace(G,'G').lower()
					all_mapped = True
					for entry in trial.split(" "):
						if ''.join(sorted([ x for x in entry ])) not in digit_map:
							all_mapped = False
							break
					if all_mapped:
						out = ''
						unk = unk.replace(A,'A').replace(B,'B').replace(C,'C').replace(D,'D').replace(E,'E').replace(F,'F').replace(G,'G').lower()
						for entry in unk.split(" "):
							out += digit_map[''.join(sorted([ x for x in entry ]))]
						all_sums += int(out)
						break
	print(all_sums)

