# travelling saleman problem

# fibonacci direct implementation
def fib_direct(n):
  if n <=2: return 1
  else:
      return fib(n-1) + fib(n-2)

# using list
def fib_list(n):
  fibValues = [0,1]
  for i in range(2,n+1):
    fibValues.append(fibValue[i-1]+fibValue[i-2])
  return fibValues[n]

# coin change algorithm
# what is the smallest number of coins I can use to make exact change ?
# the best way to make change for thirty cents if you have quarters, dimes and pennies, would be to use three dimes
# as opposed to a quarter and five pennies. So that greedy algorithm doesn't work here.

def coinChange(centsNeeded, coinValues):
  minCoins = [[0 for j in xrange(centsNeeded+1)] for i in xrange(len(coinValues))]
  minCoins[0] = xrange(centsNeeded+1)
  
  for i in xrange(1,len(coinValues)):
    for j in xrange(0, centsNeeded+1):
      if j < coinValues[i]:
        minCoins[i][j] = minCoins[i-1][j]
      else:
        minCoins[i][j] = min(minCoins[i-1][j], 1+minCoins[i][j-coinValues[i]])
  return minCoins[-1][-1]

def solve_tsp_dynamic(points):
  '''
  using dynamic programming
  '''
  # calculate all lengths
  all_distances = [[length(x,y) for y in points] for x in points]
  # initial value- just distance from 0 to every other point + keep the track of edges
  A = {(frozenset([0, idx+1]), idx+1): (dist, [0, idx+1]) for idx, dist in enumerate(all_distances[0][1:])}
  cnt = len(points)
  for m in xrange(2,cnt):
    B = {}
    for S in [frozenset(C) | {0} for C in itertools.combinations(range(1,cnt),m)]:
      for j in S-{0}:
        B[(S,j)] = min([(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k!=0 and k!=j])
        # this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
    A = B
  res = min(([A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
  return res[1]

