#
import numpy as np
import matplotlib.pyplot as plt

def main():
  print('DMRL v0.0.1 build 1')
  x = np.linspace(0, 10, 100)
  fig = plt.figure()
  plt.plot(x, np.sin(x), '-')
  plt.plot(x, np.cos(x), '--')

if '__main__' == __name__:
  main()
