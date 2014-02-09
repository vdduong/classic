# Pebble basic: markov chain and Monter Carlo algorithm

import random

# basic: moving right, left, down and up

neighbor = [[1,3,0,0], [2,4,0,1],[2,5,1,2],
            [4,6,3,0], [5,7,3,1],[5,8,4,2],
            [7,6,6,3], [8,7,6,4],[8,8,7,5]]

t_max = 4
site = 8
t = 0
print site
while t < t_max:
  t+=1
  site = neighbor[site][random.randint(0,3)]
  print site

# convergence to a steady state, multirun

N_runs = 25600
for run in range(N_runs):
  site = 8
  t = 0
  while t<t_max:
    t+=1
    site = neighbor[site][random.randit(0,3)]
  print site
  
# Pebble multirun histogram ?

# transfer matrix method allows to solve the 3x3 peeble problem, p(a->b) ..
# Peeble transfer
import numpy

transfer = numpy.zeros((9,9))
for k in range(9):
  for neigh in range(4): transfer[neighbor[k][neigh], k] +=0.25

position = numpy.zeros(9)
position[8] = 1.0
for t in range(100):
  print t, ' ', ['%0.5f'%i for i in position]
  position = numpy.dot(transfer, position)

# using eigenvalue: equilibrium position vector is in fact the eigenvector of the matrix with eigenvalue equals 1

eigenvalues, eigenvectors = numpy.linalg.eig(transfer)
print eigenvalues # eigenvalues = [1.00, 0.75 ..]



# movie ?






















