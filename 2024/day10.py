t = dict()

y = 0

def bfs(pt):
 seen = set()
 seen.add(pt)
 q = [pt]
 tops = 0
 while q:
  pos = q.pop(0)
  x, y = pos
  if t[pos] == 9:
   tops += 1
  else:
   for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
    np = (x+dx,y+dy)
    if np in t and np not in seen and t[np] == t[pos] + 1:
     q.append(np)
     seen.add(np)
 return tops
   
def dfs(pt, parent=None):
 if t[pt] == 9: return 1
 path_total = 0
 for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
  np = (pt[0]+dx,pt[1]+dy)
  if np != parent and np in t and t[np] == t[pt]+1:
   path_total += dfs(np, pt)
 return path_total
 
 

with open('input.txt','r') as infile:
 for line in infile:
  for x,char in enumerate(line.strip()):
   t[(x,y)] = int(char)
  y += 1

total = 0
for pt in t.keys():
 if t[pt] == 0:
  total += bfs(pt)
print(total)

total = 0
for pt in t.keys():
 if t[pt] == 0:
  total += dfs(pt)
print(total)

