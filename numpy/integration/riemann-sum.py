import numpy as np
import math


dx = 0.001
xi = np.arange(0, math.pi/2, dx)


xip = (xi[1:] + xi[:-1]) / 2
s = np.sum(np.sin(xip) * dx)
print(f"Riemann sum: {s}, x0: {xi[0]}, xn: {xi[-1]}")
