# Longest commun sequence
# mutiple applications: molecular biology, spelling correction ..
# three choices when the first characters differ:
# remove from either string or remove from both
# then again a recursive problem
# here, we employ dynamic programming

def lcs(a,b):
  
