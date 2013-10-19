# multilayer perceptron by N. Rougier

#-------------------------------------------------
import numpy as np

def sigmoid(x):
  return np.tanh(x)

def dsigmoid(x):
  return 1.0 - x**2

class MLP:
  def __init__(self, *args):
    self.shape = args
    n = len(args)
    
    # build layers
    self.layers = []
    # input layers (+1 for bias)
    self.layers.append(np.ones(self.shape[0]+1))
    # hidden layers + output layer
    for i in range(1,n):
      self.layers.append(np.ones(self.shape[i]))
    
    # build weights matrix
    self.weights = []
    for i in range(n-1):
      self.weights.append(np.zeros(self.layers[i].size, self.layers[i+1].size))
    
    # dw hold last change in weights (for momentum)
    self.dw = [0,]*len(self.weights)
    
    # reset weights
    self.reset()
  
  def reset(self):
    for i in range(len(self.weights)):
      Z = np.random.random((self.layers[i].size, self.layers[i+1].size))
      self.weights[i][...] = (2*Z - 1)*0.25
      
  def propagate_forward(self, target, lrate=0.1, momentum=0.1):
    deltas = []
    
    # compute error on output layer
    error = target - self.layers[-1]
    delta = error*dsigmoid(self.layers[-1])
    deltas.append(delta)
    
    # compute error on hidden layers
    for i in range(len(self.shape)-2,0,-1):
      delta = np.dot(deltas[0], self.weights[i].T)*dsigmoid(self.layers[i])
      deltas.insert(0, delta)
    
    # update weights:
    for i in range(len(self.weights)):
      layer = np.atleast_2d(self.layers[i])
      delta = np.atleast_2d(deltas[i])
      dw = np.dot(layer.T, delta)
      self.weights[i] += lrate*dw + momentum*self.dw[i]
      self.dw[i] = dw
      
    # return error
    return (error**2).sum()
    
