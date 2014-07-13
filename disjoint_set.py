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
      
