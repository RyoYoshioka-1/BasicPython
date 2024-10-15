from math import sin
import numpy as np
# --example--
# print(sin(0))
# >>> 0
# -----------


a = 0  
b = np.pi / 2  
n = 100  

h = (b - a) / n

x = np.linspace(a, b, n + 1)

y = np.sin(x)

integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
integral
