# disjoint sets 
# the set of sets is stored as an array of integers.
# if at position i the array stores a negative number, this number is interpreted as being the representative element of its own set
# if the number stored at position i is instead a nonnegative number j, it means that it belongs to a set that was joined with the set containing j

class DisjointSets(object):
  def __init__(self, n):
    self.sets = [-1]*n
    self.counter = n
  
  def parent(self, i):
    while True:
      j = self.sets[i]
      if j <0:
        return i
      i = j
  
  def join(self, i,j):
    i,j = self.parent(i), self.parent(j)
    if i !=j:
      self.sets[i]+=self.sets[j]
      self.sets[j] = i
      self.counter-=1
      return True
    return False
  
  def joined(self,i,j):
    return self.parent(i) == self.parent(j)
  
  def __len(__(self):
    return self.counter
      
# Kruskal algorithm

def Kruskal(graph):
  vertices, links = graph
  A = []
  S = DisjointSets(len(vertices))
  links.sort(cmp=lambda a,b: cmp(a[2],b[2]))
  for source, dest, length in links:
    if S.join(source, dest):
      A.append((source, dest, length))
  return A

# Prim
# works on direct graphs
# does need a starting vertex

class PrimVertex(object):
  INFINITY = 1e100
  def __init__(self, id, links):
    self.id = id
    self.closest = None
    self.closest_dist = PrimVertex.INFINITY
    self.neighbors = [link[1:] for link in links if link[0] ==id]
  def __cmp__(self, other):
    return cmp(self.closest_dist, other.closest_dist)

def Prim(graph, start):
  from heapq import heappush, heappop, heapify
  vertices, links = graph
  P = [PrimVertex(i, links) for i in vertices]
  Q = [P[i] for i in vertices if not i ==start]
  vertex = P[start]
  while Q:
    for neighbor_id, length in vertex.neighbors:
      neighbor = P[neighbor_id]
      if neighbor in Q and length < neighbor.closest_dist:
        neighbor.closest = vertex
        neighbor.closest_dist = length
    heapify(Q)
    vertex = heappop(Q)
  return [(v.id, v.closest.id, v.closest_dist) for v in P if not v.id == start]
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  
  
  
