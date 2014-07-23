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
# neurons are usually organized in the layers with one input layer of neurons connected only with the input and the next
# output layer & many hidden layers
# each neuron is defined by a set of parameters a which determined the relative weight of the input signals
# the network is trained iteratively until its parameters converge (if they converge) and then it's ready to make predictions

class NeuralNetwork:
  '''
  back propagation neural networks
  Neil Schemenauer, Massimo Di Pierro
  '''
  @staticmethod
  def rand(a,b):
    '''calculate a random number where a<=rand<=b'''
    return (b-a)*random.random()+a
  @staticmethod
  def sigmoid(x):
    return math.tanh(x)
  @staticmethod
  def dsigmoid(x):
    return 1.0-x**2
  
  def __init__(self,ni,nh,no):
    # numbers of input, hidden, and output nodes
    self.ni = ni+1 # +1 for bias node
    self.nh = nh
    self.no = no
    
    # activations for nodes
    self.ai = [1.0]*self.ni
    self.ah = [1.0]*self.nh
    self.ao = [1.0]*self.no
    
    # create weights
    self.wi = Matrix(self.ni, self.nh, fill=lambda r,c: self.rand(-0.2, 0.2))
    self.wo = Matrix(self.nh, self.no, fill=lambda r,c: self.rand(-2.0, 2.0))
    
    # last change in weights for momentum
    self.ci = Matrix(self.ni, self.nh)
    self.co = Matrix(self.nh, self.no)
  
  def update(self, inputs):
    if len(inputs) != self.ni-1:
      raise ValueError('wrong number of inputs')
    
    # input activations
    for i in xrange(self.ni-1):
      self.ai[i]=inputs[i]
    
    # hidden activations
    for j in xrange(self.nh):
      s = sum(self.ai[i]*self.wi[i,j] for i in xrange(self.ni))
      self.ah[j] = self.sigmoid(s)
    
    # output activations
    for k in xrange(self.no):
      s = sum(self.ah[j]*self.wo[j,k] for j in xrange(self.nh))
      self.ao[k] = self.sigmoid(s)
    return self.ao[:]
  
  def back_propagate(self, targets, N, M):
    return error
  
  def test(self, patterns):
    return None
  
  def weights(self):
    print('Input weights:')
    for i in xrange(self.ni):
      print(self.wi[i])
    print
    print('Output weights:')
    for j in xrange(self.nh):
      print(self.wo[j])
  
  def train(self, patterns, iterations = 1000, N=0.5, M=0.1, check=False):
    return None
  

# GENETIC ALGORITHM
          
          
          
          
          
          
      
