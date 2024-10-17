from math import sin, exp
import numpy as np

def integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)  

    result = (h / 2) * (fx[0] + 2 * np.sum(fx[1:n]) + fx[n])
    return result

# (1) np.sinを使用した例
result = integral(np.sin, 0, np.pi/2, 50)
print(f"(1) Result is {result}.")

# (2) 4/(1 + x^2) の積分
result = integral(lambda x: 4 / (1 + x**2), 0, 1, 50)
print(f"(2) Result is {result}.")

# (3) sqrt(π) * exp(−x^2) の積分
result = integral(lambda x: np.sqrt(np.pi) * np.exp(-x**2), -100, 100, 1000)
print(f"(3) Result is {result}.")



