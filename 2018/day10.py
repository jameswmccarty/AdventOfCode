#!/usr/bin/python

from PIL import Image

class Point:
	
	def __init__(self, x, y, dx, dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.ox = x
		self.oy = y
	
	def move(self):
		self.x += self.dx
		self.y += self.dy
		
	def set_time(self, t):
		self.x = self.ox + self.dx*t
		self.y = self.oy + self.dy*t
	

def parse_pt(line):
	# Example: position=< 9,  1> velocity=< 0,  2>
	pos, vol = line.split("> velocity=<")
	pos = pos.replace("position=<", '').strip()
	x, y = pos.split(",")
	vol = vol.replace(">", '').strip()
	dx, dy = vol.split(",")
	return Point(int(x),int(y),int(dx),int(dy))
	
def draw_sky(w, h, points):
	#line = '-' * w
	#print line
	sky = [[" "] * w for i in range(h)]
	for p in points:
		if p.y >=0 and p.y < h and p.x >=0 and p.x < w:
			sky[p.y][p.x] = "X"
	for row in sky:
		line = ''.join(val for val in row)
		print line.rstrip()

def img_sky(w,h,points):
	img = Image.new( 'RGB', (w,h), "black") # Create a new black image
	pixels = img.load() # Create the pixel map
	for p in points:
		if p.x >=0 and p.x < w and p.y >=0 and p.y < h:
			pixels[p.x,p.y] = (255, 255, 255) # Set the colour accordingly
	return img
	
# translate points to origin and return
# overall width and height
def clean_dim(points):
	mx = 10000
	my = 10000
	ax = 0
	ay = 0
	for p in points:
		mx = min(p.x,mx)
		my = min(p.y,my)
	for p in points:
		p.x -= mx
		p.y -= my
		ay = max(p.y,ay)
		ax = max(p.x,ax)
	return ax, ay

# alignment occurs when all characters are less than 10 pixels tall
def guess_jump(t, points):
	mn = 1000
	mx = 0
	for p in points:
		p.set_time(t)
		mn = min(mn,p.y)
		mx = max(mx,p.y)
	if mx-mn < 10:
		return True
	return False
	

if __name__ == "__main__":

	# Part 1 and 2 Solution
	
	points = []
	
	with open("day10_input", "r") as infile:
		for line in infile.readlines():
			points.append(parse_pt(line))
			
	jump_t = 0
	for i in range(25000):
		if guess_jump(i,points):
			jump_t = i
			break
	
	w,h = clean_dim(points)
	
	draw_sky(w+2,h+2,points)
	print jump_t
	img_sky(w+2,h+2,points).show()
