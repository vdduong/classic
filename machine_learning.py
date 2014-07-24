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
    if len(targets)!=self.no:
      raise ValueError('wrong number of target values')
    # calculate error terms for output
    output_deltas = [0.0]*self.no
    for k in xrange(self.no):
      error = targets[k]-self.ao[k]
      output_deltas[k] = self.dsigmoid(self.ao[k])*error
    # calculate error terms for hidden
    hidden_deltas = [0.0]*self.nh
    for j in xrange(self.nh):
      error = sum(output_deltas[k]*self.wo[j,k] for k in xrange(self.no))
      hidden_deltas[j] = self.dsigmoid(self.ah[j])*error
    # update output weights
    for j in xrange(self.nh):
      for k in xrange(self.no):
        change = output_deltas[k]*self.ah[j]
        self.wo[j,k] = self.wo[j,k] + N*change + M*self.co[j,k]
        self.co[j,k] = change
    # update input weights
    for i in xrange(self.ni):
      for j in xrange(self.nh):
        change = hidden_deltas[j]*self.ai[i]
        self.wi[i,j] = self.wi[i,j] + N*change + M*self.ci[i,j]
        self.ci[i,j] = change
    # calculate error
    error = sum(0.5*(targets[k]-self.ao[k])**2 for k in xrange(len(targets)))
    return error
  
  def test(self, patterns):
    for p in patterns:
      print(p[0], '->', self.update(p[0]))
  
  def weights(self):
    print('Input weights:')
    for i in xrange(self.ni):
      print(self.wi[i])
    print
    print('Output weights:')
    for j in xrange(self.nh):
      print(self.wo[j])
  
  def train(self, patterns, iterations = 1000, N=0.5, M=0.1, check=False):
    # N learning rate
    # M momentum factor
    for i in xrange(iterations):
      error = 0.0
      for p in patterns:
        inputs = p[0]
        targets = p[1]
        self.update(inputs)
        error = error + self.back_propagate(targets, N, M)
      if check and i%100==0:
        print('error %-14f'%error)
  
# GENETIC ALGORITHM
# the algorithm stops when we reach a maximum number of generations or we find a chromosome with max fitness

from random import randint, choice

class Chromosome:
  alphabet = 'ATGC'
  size = 32
  mutations = 2
  def __init__(self, father=None,mother=None):
    if not father or not mother:
      self.dna = [choice(self.alphabet) for i in xrange(self.size)]
    else:
      self.dna = father.dna[:self.size/2]+mother.dna[self.size/2:]
      for mutation in xrange(self.mutations):
        self.dna[randint(0,self.size-1)] = choice(self.alphabet)
  def fitness(self, target):
    return sum(1 for i,c in enumerate(self.dna) if c==target.dna[i])
          
          
          
          
          
          
      
