# knapsack problem

# continuous knapsack
# f = a0*x0 + .. + an*xn
# given the constraint: b0*x0 + .. + bn*xn <= c
# can be formulated in term of financial portfolio

def continuum_knapsack(a,b,c):
  table = [(a[i]/b[i],i) for i in xrange(len(a))]
  table.sort()
  table.reverse()
  f=0.0
  for (y,i) in table:
    quantity = min(c/b[i],1)
    x.append((i, quantity))
    c=c-b[i]*quantity
    f=f+a[i]*quantity
  return (f,x)

# discrete knapsack
