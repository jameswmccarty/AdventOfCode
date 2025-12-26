#!/usr/bin/python

pixbuf = []

def findTargetLayer(w,h,img):
	fewest = float('inf')
	score  = 0
	while len(img) > 0:
		zeros = 0
		ones  = 0
		twos  = 0
		for i in range(h):
			row = img[0:w]
			img = img[w:]
			zeros += row.count('0')
			ones  += row.count('1')
			twos  += row.count('2')
		if zeros < fewest:
			fewest = zeros
			score = ones * twos
	return score

def processPixBuffer(w,h,img):
	while len(img) > 0:
		for i in range(h):
			row = img[0:w]
			img = img[w:]
			for idx, p in enumerate(row):
				if pixbuf[i][idx] == '2' and p != '2':
					pixbuf[i][idx] = p	

if __name__ == "__main__":
	
	# Part 1 Solution
	w = 25
	h = 6
	with open("day08_input", 'r') as infile:
		for line in infile.readlines():
			print(findTargetLayer(w,h,line.strip()))

	# Part 2 Solution
	for c in range(h):
		pixbuf.append(['2'] * w)
	with open("day08_input", 'r') as infile:
		for line in infile.readlines():
			processPixBuffer(w,h,line.strip())
			#processPixBuffer(2,2,'0222112222120000')	
	for row in pixbuf:
		print(''.join(row).replace('0',' '))
	
	
