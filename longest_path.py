# longest path algorithm

import string
import time

# represents a vertex in the graph:
class Vertex(object):
  def __init__(self, name):
    self.name = name
    self.visited = 0 # access flag 1 = visited, 0 = not visited

# represents an edge in the graph
class Edge:
  def __init__(self, v,u,length):
    self.start = v
    self.end = u
    self.length = length

# read a text file and generate the graph according to declarations
def generateGraph(V,E):
  file = open('graph_def_v11', 'r')
  line = file.readline()
  line = line[:-1]
  while line:
    taglist = string.split(line)
    if taglist[0] == 'vertex':
      V.append(Vertex(taglist[1]))
    elif taglist[0]=='edge':
      E.append(Edge(taglist[1], taglist[2], string.atoi(taglist)))
      E.append(Edge(taglist[2], taglist[1], string.atoi(taglist)))
    line = file.readline()
    line = line[:-1]
  file.close()

# return the edges list of vertex v
def pickEdgesList(v,E):
  vu = []
  for edge in E:
    if edge.start == v.name:
      vu.append(edge)
  return vu

def pickVertexByName(V, A):
  for vertex in V:
    if vertex.name == A:
      return vertex

def LP(V,E,A):
  dist = 0
  maxa = 0
  v= pickVertexByName(V,A)
  v.visited ) 1
  vu=pickEdgesList(v,E)
  for edge in vu:
    u = pickVertexByName(V, edge.end)
    if u.visited ==0:
      dist = edge.length +LP(V,E,u.name)
      if dist > maxa:
        maxa = dist
  v.visited = 0
  return maxa

def main():
  print('Starting longest path algorithm:')
  t1 = time.time()
  V = []
  E =[]
  generateGraph(V,E)
  maxa = LP(V,E,'a')
  print 'maax=', maxa
  t2 = time.time()
  print t2-t1

main()









