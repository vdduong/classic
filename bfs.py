# the algorithm starts by building a table of neighbors so that for each vertex, it knows which other vertices it is connected to.
# it then maintains two lists, a list of blacknodes (defined as vertices that have been visited) 
# graynodes = vertices that have been discovered because the algorithm has visited its neighbor
# return that blacknode list

def breadth_first_search(graph, start):
  vertices, link = graph
  blacknodes = []
  graynodes = [start]
  neighbors = [[] for vertex in vertices]
  for link in links:
    neighbors[link[0]].append(link[1])
  while graynodes:
    current = graynodes.pop()
    for neighbor in neighbors[current]:
      if not neighbor in blacknodes+graynodes:
        graynodes.insert(0, neighbor)
    blacknodes.append(current)
  return blacknodes
