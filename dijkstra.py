"""
algorithm of dijkstra (greedy algorithm)
- distance to source vertex is zero
- set all other distances to infinity
- S, the set of visited vertices is initially empty
- Q, the queue initially contains all vertices
- while the queue is not empty
- select the element of Q with the min distance
- add u to list of visited vertices; if new shortest path is found, set new value of shortest path.
"""

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    
  def add_node(self, value):
    self.nodes.add(value)
  
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    
  def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}
  
    nodes = set(graph.nodes)
    
    while nodes:
      min_node = None
      for node in nodes:
        if node in visited:
          if min_node is None:
            min_node = node
          elif visited[node] < visited[min_node]:
            min_node = node
            
      if min_node is None:
        break
        
      nodes.remove(min_node)
      current_weight = visited[min_node]
      
      for edge in graph.edges[min_node]:
        weight = current_weight + graph.distance[(min_node, edge)]
        if edge not in visited or weight < visited[edge]:
          visited[edge] = weight
          path[edge] = min_node
    return visited, path
    
    
def dijkstra(G, s):
    # initialize single source (G,s)
    for v in set(G.nodes):
        v.d = float('Inf')
        v.prev = None
    path = {s:0}
    Q = set(G.nodes)
    while Q:
        u = None
        # extract_min (Q)
        for node in Q:
          if node in path:
            if u == None:
              u = node
            elif path[node] < path[u]:
              u = node
        
        if u == None:
          break
                          
        Q.remove(u)
        # relaxation 
        for v in G[u].next:
          wt = path[u] + G.edges[(u,v)]
          if v not in path.keys() or wt < path[v]:
            path[v] = wt
            v.pred = u
          
          
          
          
  
