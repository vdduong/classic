# algorithm of Floyd Warshall to find all pairs of closest distance within a directed graph

def adj(g):
  """
  convert a directed graph to an adjacency matrix
  """
  vertices = g.keys()
  
  dist = {}
  for i in vertices:
    dist[i] = {}
    for j in vertices:
      try:
          dist[i][j] = g[i][j]
      except KeyError:
          # the distance from a node to itself is 0
          if i == j:
            dist[i][j] = 0
          # the distance from a node to an unconnected node is infinity
          else:
            dist[i][j] = float('inf')
  return dist
  
def fw(g):
  """
  run the Floyd Warshall algorithm on an adjacency matrix
  The FW algorithm computes the minimum cost of a simple path between each pair of vertices
  It's dynamic programming
  """
  
  vertices = g.keys()
  
  d = dict(g)
  for k in vertices:
    for i in vertices:
      for j in vertices:
        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  return d
  

  
  
