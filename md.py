# molecular dynamics

import random
import numpy

def initialization(N_atoms, L):
  for i in xrange(N_atoms):
    for j in xrange(3):
      xyz[i][j] = random.random()*L # L is the dimension, xyz the box
      v[i][j] = random.random()-0.5 # velocity
  return xyz, v
  
def force():
  aL = 1./float(L)
  f = 0.0
  for i in xrange(N_atoms-1):
    for j in xrange(i+1, N_atoms):
      dr[1:3] = xyz[1:3][i] - xyz[1:3][j] # 1=x, 2=y,3=z
      dr[1:3] = dr[1:3] - round(dr[1:3]*aL)
      r2 = dr[1]**2. + dr[2]**2. + dr[3]**2.
      r2i = 1./r2
      r6i = r2i**3.
      ff[1:3] = r2i*r6i*(r6i-0.5)
      for idim in xrange(3):
        f[i][idim] = f[i][idim] + ff[idim]*dr[idim]
        f[j][idim] = f[j][idim] - ff[idim]*dr[idim]
      en = en + r6i*(r6i-1.)
  f = 48.*f
  en = 4.*en
  return f, en

def updating():
  for i in xrange(N_atoms):
    for j in xrange(3):
      xyz[i][j]+= delta_t*v[i][j] + f[i][j]*delta_t**2./2.
      v[i][j] += delta_t*0.5*(f[i][j] t and t+delta_t)
  return xyz, v
