# Longest commun sequence
# mutiple applications: molecular biology, spelling correction ..
# three choices when the first characters differ:
# remove from either string or remove from both
# then again a recursive problem
# here, we employ dynamic programming

def lcs(a,b):
  previous = [0]*len(a)
  for i,r in enumerate(a):
    current = []
    for j,c in enumerate(b):
      if r==c:
        e = previous[j-1]+1 if i*j>0 else 1
      else:
        e = max(previous[j] if i>0 else 0, current[-1] if j>0 else 0)
      current.append(e)
    previous=current
  return current[-1]

# Fibonnaci direct implemtation in Python
def fib(n):
  if n<=2:
    return 1
  else:
    return fib(n-1)+fib(n-2)

# using tuple ?
def fib(n):
  fibValues = [0,1]
  for i in range(2,n+1):
    fibValues.append(fibValues[i-1]+fibValues[i-2])
  return fibValues[n]

fibTable = {1:1, 2:1}
def fib(n):
  if n<=2:
    return 1
  if n in fibTable:
    return fibTable[n]
  else:
    fibTable[n]=fib(n-1)+fib(n-2)
    return fibTable[n]


# algorithm via wikipedia
def lcs_new(i,j): # i = position in sequence a and j = position in sequence b
  if i==0 or j==0:
    return []
  else:
    if a[i]==b[j]:
      return lcs_new(i-1,j-1)+1
    else:
      return max(lcs_new(i-1,j), lcs_new(i,j-1))
  
# Needleman Wunsch algorithm
# solves the problem of global sequence alignment
# when two matching symbols are found and they are not consecutive, penalty equal to pˆm

def needleman_wunsch(a,b,p=0.97):
  z=[]
  for i,r in enumerate(a):
    z.append([])
    for j,c in enumerate(b):
      if r==c:
        e = z[i-1][j-1]+1 if i*j>0 else 1
      else:
        e = p*max(z[i-1][j] if i>0 else 0, z[i][j-1] if j>0 else 0)
      z[-1].append(e)
  return z

# application
bases = 'ATGC'
from random import choice
genes = [''.join(choice(bases) for k in xrange(10)) for i in xrange(20)]
chromosome1 = ''.join(choice(genes) for i in xrange(10))
chromosome2 = ''.join(choice(genes) for i in xrange(10))
z = needleman_wunsch(chromosome1, chromosome2)
canvas(title='Needleman Wunsch').imshoz(z).save('images/needleman.png')


      
      
      
      
      
      
      





