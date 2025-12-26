test='125 17'

with open('day11_input','r') as infile:
 inp=infile.read().strip()

def p(n):
 if n==0: return [1]
 if len(str(n))%2 == 0:
  a=str(n)
  return [int(a[0:len(a)//2]), int(a[len(a)//2:])]
 return [2024*n]

a = [*map(int,inp.split())]

for z in range(25):
 b=[]
 for n in a:
  b.extend(p(n))
 a = b
print(len(a))

counts = dict()

def gen(d):
 n = dict()
 for value, count in d.items():
  for x in p(value):
   if x not in n:
    n[x] = 0
   n[x] += count
 return n

a = [*map(int,inp.split())]
for x in a:
 counts[x] = 1

for _ in range(75):
 counts = gen(counts)
print(sum(counts.values()))
