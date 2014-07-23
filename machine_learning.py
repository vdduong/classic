# some algorithms for machine learning

# CLUSTERING algorithms: 3 types: hierarchical, centroid-based and distribution based clustering.

class Cluster(object):
  def __init__(self, points,metric,weights=None):
    self.points, self.metric = points, metric
    self.k = len(points)
    self.w = weights or [1.0]*self.k
    self.q = dict((i,[i]) for i,e in enumerate(points))
    self.d = []
    for i in xrange(self.k):
      for j in xrange(i+1, self.k):
        m = metric(points[i], points[j])
        if not m is None:
          self.d.append((m,i,j))
    self.d.sort()
    self.dd = []
  
  def parent(self,i):
    while isinstance(i,int): (parent,i)=(i,self.q[i])
    return parent, i
  
  def step(self):
    if self.k>1:
      # find new clusters to join
      (self.r,i,j), self.d = self.d[0], self.d[1:]
      # join them
      i,x = self.parent(i) # find members of cluster i
      j,y = self.parent(j) # find members of cluster j
      x+=y
      self.q[j] = i # make j cluster point to i
      self.k-=1 # decrease cluster count
      # update all distances to new joined cluster
      new_d = [] # links not related to joined cluster
      old_d = {} # old links related to joined cluster
      for (r,h,k) in self.d:
        if h in (i,j):
          a,b = old_d.get(h, (0.0,0.0))
          old_d[k] = a+self.w[k]*r, b+self.w[k]
        elif k in (i,j):
          a,b = old_d.get(h,(0.0,0.0))
          old_d[h] = a+self.w[h]*r, b+self.w[h]
        else:
          new_d.append((r,h,k))
      new_d+=[(a/b,i,k) for k,(a,b) in old_d.items()]
      new_d.sort()
      self.d = new_d
      # update weight of new cluster
      self.w[i] = self.w[i]+self.w[j]
      # get new list of cluster members
      self.v = [s for s in self.q.values() if isinstance(s,list)]
      self.dd.append((self.r, len(self.v)))
    return self.r, self.v
    
  def find(self,k):
    # if necessary, start again
    if self.k < k: self.__init__(self.points, self.metric)
    # step until we get k clusters
    while self.k>k: self.step()
    # return list of cluster members
    return self.r, self.v

# NEURAL NETWORK

# GENETIC ALGORITHM
          
          
          
          
          
          
      
