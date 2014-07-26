# data structures in Python

# arrays
# list: in Python, what is called a list is actually an array of pointers to the elements

# stack
# is a container, and it is usually implemented as a list. 
" it has the property that the first thing you can take out is the last thing put in, commonly known as LIFO
# the method to insert or add data to the container is called 'push'
# and the method to extract data is called 'pop'

stk =[]
stk.append("One")
stk.append("Two")
print stk.pop() # Two

# queue or FIFO
que = []
que.insert(0,"One")
que.insert(0,"Two")
print que.pop() # One
que.insert(0, "Three")
print que.pop() # Two
print que.pop() # Three

# the Python package collection.deque is designed to implement queues and stacls
# for a stack, use .pop to return the most recent item added
# for a queue, .popleft to remove the oldest to remove the oldest item in the list

from collections import deque
que = deque([])
que.append("One")
que.append("Two")
print que.popleft() # One
que.append("Three")
print que.popleft() # Two
print que.popleft() # Three

# sorting

def quicksort(A, p=0,r=-1):
  if r is -1:
    r=len(A)
  if p<r-1:
    q= partition(A,p,r)
    quicksort(A,p,q)
    quicksort(A,q+1,r)

def partition(A,i,j):
  x=A[i]
  h=i
  for k in xrange(i+1,j):
    if A[k]<x:
      h=h+1
      A[h],A[k] = A[k],A[h]
  A[h],A[i] = A[i],A[h]
  return h
  
# the quicksort can also be randomized by picking pivot A[r] at random
def quicksort(A, p=0,r=-1):
  if r is -1:
    r=len(A)
  if p<r-1:
    q=random.randint(p,r-1)
    A[p],A[q] = A[q],A[p]
    q= partition(A,p,r)
    quicksort(A,p,q)
    quicksort(A,q+1,r)

# the counting sort
def counting_sort(A):
  if min(A)<0:
    raise '_counting sort List Unbound'
  i,n,k = 0, len(A), max(A)+1
  C = [0]*k
  for j in xrange(n):
    C[A[j]] = C[A[j]] +1
  for j in xrange(k):
    while C[j] >0:
      (A[i],C[j],i) =(j, C[j]-1,i+1)
  


















