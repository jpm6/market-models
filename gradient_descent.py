from random import random 
import numpy as np

dot = np.dot
g   = np.gradient

add = lambda v1,v2: [x + y for x, y in zip(v1, v2)]
mul = lambda v1,v2: [x * y for x, y in zip(v1, v2)]

norm = lambda v,n: sum([i ** n for i in v]) ** (1 / n)
dis = lambda v1,v2: 0.5 * norm([x - y for x, y in zip(v1, v2)],2) ** 2

# Diameter - ||x1 - x2|| <= D
D = 2

# Instance Dimensions
d = 2

# Objective Function => min ||Ax + b||^2
A = [1.0] * d
b = [0.0] * d

f = lambda x: norm(add(mul(A,x),b),2) ** 2

# Iterations
k = 10

# Lipschitz Constant
L = 2 * (norm(b,1) + D * norm(A,2)) * norm(A,2)

# Gamma
gamma = 1 / L

# x_0
r = lambda i: random() * 2 - 1
sample = lambda: list(map(r, range(d)))

x = sample()

for t in range(k):
    print("f(x):\t %.3f" % f(x))
    print("x:\t", ['%.3f' % i for i in x])
    print("g(x):\t", ['%.3f' % (-gamma * i) for i in g(x)])
    print('')

    x = add(x, -gamma * g(x))
    #s = sample()
    #x = gamma * dot(g(x),s) + dis(s,x) 

    for i in range(d):
        if    x[i] > 1 : x[i] = 1
        elif  x[i] < -1: x[i] = -1

def g(x):
    e = [-gamma,0,gamma]
    for i in e:
        for j in e:

