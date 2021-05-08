import numpy as np
import math

xi = np.arange(0, math.pi/2, 0.1)

print(xi)

deriv = (np.sin(xi + 0.1) - np.sin(xi - 0.1)) / (2*0.1)
print(deriv)