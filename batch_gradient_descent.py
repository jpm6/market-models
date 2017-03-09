from random import random 
import numpy as np

norm = np.linalg.norm

# Diameter - ||x1 - x2|| <= D
D = 2

# Instance Dimensions
d = 2

# Objective Function => min ||Ax + b||^2
A = np.ones(d)
b = np.zeros(d)

f = lambda x: norm(A * x + b) ** 2
fi = lambda x: (A * x + b) ** 2

h = .00000001

g = lambda x: (fi(x + h) - fi(x - h)) / h * .5

# Iterations
k = 10

# Lipschitz Constant
L = 2 * (norm(b,1) + D * norm(A,2)) * norm(A,2)

# Gamma
gamma = 1 / L

# x_0
r = np.vectorize(lambda i: random() * 2 - 1)
sample = lambda: r(range(d))

x = sample()

for t in range(k):
    print("f(x):\t %.3f" % f(x))
    print("x:\t", ['%.3f' % i for i in x])
    print("step:\t", ['%.3f' % i for i in -gamma * g(x)])
    print('')

    x = x - gamma * g(x)
    #s = sample()
    #x = gamma * dot(g(x),s) + dis(s,x) 
