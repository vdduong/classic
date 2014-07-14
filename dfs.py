# deep first search

def depth_first_search(graph, start):
  vertices, link = graph
  blacknodes =[]
  graynodes = [start]
  neighbors = [[] for vertex in vertices]
  for link in links:
    neighbors[link[0]].append(link[1])
  while graynodes:
    current = graynodes.pop()
    for neighbor in neighbors[current]:
      if not neighbor in blacknodes+graynodes:
        graynodes.append(neighbor)
    blacknodes.append(current)
  return blacknodes
