from random import random 
import numpy as np

norm = np.linalg.norm

# Define Set
r = np.vectorize(lambda i: random() * 2 - 1)
sample = lambda: r(range(d))

# Diameter - ||x1 - x2|| <= D
D = 2

# Instance Dimensions
d = 5

# Objective Function => min ||Ax + b||^2
A = np.ones(d)
b = np.zeros(d)

f = lambda x: norm(A * x + b) ** 2

# Attribute Function for Gradients
a = lambda x: (A * x + b) ** 2

# Small Number
h = .00000001

# Centered Distance Formula
g = lambda x: (a(x + h) - a(x - h)) / (2 * h)

# Iterations
k = 10

# Lipschitz Constant
L = 2 * (norm(b,1) + D * norm(A)) * norm(A)

# Gamma
gamma = 1 / L

# Random Sample for x_0
x = sample()

for t in range(k):
    print('Iteration:', t, '\n')
    print("x:\t", ['%.5f' % i for i in x])
    print("f(x):\t %.5f" % f(x))
    print("step:\t", ['%.5f' % i for i in -gamma * g(x)], '\n')

    x = x - gamma * g(x)
    #s = sample()
    #x = gamma * dot(g(x),s) + dis(s,x) 
