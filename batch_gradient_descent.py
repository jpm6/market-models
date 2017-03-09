from random import random 
import numpy as np

norm = np.linalg.norm

# Diameter: max ||x1 - x2|| for x1,x2 in X
D = 2

# Define Set
r = np.vectorize(lambda i: random() * D - D/2)
sample = lambda: r(range(d))

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
k = 20

# Lipschitz Constant
L = 2 * (norm(b,1) + D * norm(A)) * norm(A)

# Step Size modifier Gamma
gamma = 1 / L

# Random Sample for x_0
x = sample()

for t in range(k):
    print('----',t)
    print("x:\t", ['%.3f' % i for i in x])
    print("f(x):\t %.5f" % f(x))
    print("step:\t", ['%.3f' % i for i in -gamma * g(x)], '\n')

    x = x - gamma * g(x)
    #s = sample()
    #x = gamma * dot(g(x),s) + dis(s,x) 
