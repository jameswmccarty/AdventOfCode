net = dict()
trios = set()
with open('input.txt','r') as infile:
 for line in infile:
  l,r = line.strip().split('-')
  if l not in net: net[l] = set()
  if r not in net: net[r] = set()
  net[l].add(r)
  net[r].add(l)

ts = { k for k in net.keys() if k[0] == 't' }
for a in ts:
 for b in net[a]:
  for c in net[b]:
   if a in net[c]:
    trios.add(tuple(sorted([a,b,c])))
print(len(trios))

vertices = list()
degrees = list()

def find_max_clique():
	search_vert = set(vertices)
	n_edges = list(edges)
	for i in range(3,max(degrees)+2):
		last_set = set(n_edges)
		next_edges = set() # build the 'i' sized clique
		search_vert = { v for idx,v in enumerate(vertices) if degrees[idx] >= i-1 }
		while len(n_edges) > 0:
			e = n_edges.pop()
			for v in search_vert:
				if all( tuple(sorted([v,e[j]])) in edges for j in range(i-1) ):
					next_edges.add(tuple(sorted(list(e)+[v])))
		n_edges = list(next_edges)
		if len(n_edges) == 0:
			return last_set
	return n_edges

edges = set()
sort_edges = sorted(net.keys())
vertex_count = len(sort_edges)
for i in range(len(sort_edges)):
	vertices.append(i)
	degree = 0
	for j in range(i+1,vertex_count):
		if sort_edges[j] in net[sort_edges[i]]:
			edges.add(tuple(sorted([i,j])))

for i in range(vertex_count):
	degree = 0
	for j in range(vertex_count):
		if tuple(sorted([i,j])) in edges:
			degree += 1
	degrees.append(degree)

sol = find_max_clique()
print(sol)
for s in sol:
 p = [ sort_edges[e] for e in s ]
 print(','.join(sorted(p)))

