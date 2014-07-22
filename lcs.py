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


