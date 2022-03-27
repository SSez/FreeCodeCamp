import numpy as np

def calculate(inputList):
  if(len(inputList) != 9):
      raise ValueError("List must contain nine numbers.")
      return

  nlist = np.reshape(inputList, (3,3))
  mean = [ list(nlist.mean(0)), list(nlist.mean(1)), nlist.mean() ]
  variance = [ list(nlist.var(0)), list(nlist.var(1)), nlist.var() ]
  std = [ list(nlist.std(0)), list(nlist.std(1)), nlist.std() ]
  max = [ list(nlist.max(0)), list(nlist.max(1)), nlist.max() ]
  min = [ list(nlist.min(0)), list(nlist.min(1)), nlist.min() ]
  sum = [ list(nlist.sum(0)), list(nlist.sum(1)), nlist.sum() ]

  return {
    'mean': mean,
    'variance': variance,
    'standard deviation': std,
    'max': max,
    'min': min,
    'sum': sum
  }
