import numpy as np
import matplotlib.pyplot as plt
from os import path

data = np.loadtxt(path.join(path.dirname(__file__), 'points_circle.dat'))
plt.plot(data[:,0], data[:,1], 'o')

vector = np.array((2.1, 1.1))
data_trans = data + vector
plt.plot(data_trans[:,0], data_trans[:,1], 'd')

plt.savefig(path.join(path.dirname(__file__), 'result.png'))