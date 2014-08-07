# genetic algorithm to optimize a simple prob
# Trying to create a list of N numbers that equal X when summed together

# ingredients of the solution
# each suggested solution for a genetic algorithm is referred to as an individual.
# in our current problem, each list of N numbers is an individual

from random import randint
def individual(length, min, max):
  '''create a member of the population'''
  return [randint(min, max) for x in xrange(length)]

# the collection of individuals is referred to as our population
def population(count, length, min, max):
  return [individual(length, min, max) for x in xrange(count)]

# need a way to judge the how effective each solution is = fitness
# we want the fitness to be a function of the distance between the sum of an individuals numbers and the target 

from operator import add
def fitness(individual, target):
  sum = reduce(add, individual, 0)
  return abs(target-sum)

# a function that determines a populations's average fitness
def grade(pop, target):
  '''find average fitness for a population'''
  summed = reduce(add, (fitness(x, target) for x in pop), 0)
  return summed/(len(pop)*1.0)

# evolution
def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
  graded = [(fitness(x, target), x) for x in pop]
  graded = [x[1] for x in sorted(graded)]
  retain_length = int(len(graded)*retain)
  parents = graded[:retain_length] # take the bests
  
  # randomly add other individuals to promote genetic diversity
  for individual in graded[retain_length:]:
    if random_select > random():
      parents.append(individual)
  # mutate some individuals
  for individual in parents:
    if mutate > random():
      pos_to_mutate = randint(0, len(individual)-1)
      # this mutation is not ideal, because it restricts the range of possible values
      individual[pos_to_mutate] = randint(min(individual), max(individual))
  
  # cross over parents to create children
  parents_length = len(parents)
  desired_length = len(pop) - parents_length
  children = []
  while len(children) < desired_length:
    male = randint(0, parents_length-1)
    female = randint(0, parents_length-1)
    if male != female:
      male = parents[male]
      female = parents[female]
      half = len(male)/2
      child = male[:half]+female[half:]
      children.append(child)
  parents.extend(children)
  return parents
  

  
