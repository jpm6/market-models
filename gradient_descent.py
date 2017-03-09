from random     import random   as r 
from numpy      import gradient as g

add = lambda v1,v2: [x + y for x, y in zip(v1, v2)]
mul = lambda v1,v2: [x * y for x, y in zip(v1, v2)]

norm = lambda v,n: sum([i ** n for i in v]) ** (1 / n)

# Diameter - ||x|| <= D
D = 1

# Instance Dimensions
d = 10

# Objective Function => min ||Ax + b||^2
A = [0.001] * d
b = [0.001] * d

# Iterations
k = 5

# Lipschitz Constant
L = 2 * (norm(b,1) + D * norm(A,2)) * norm(A,2)

# Gamma

gamma = lambda t : (D ** 2 / (k * L ** 2)) ** 0.5

# x_0
x = list(map(lambda i: r() * 2 - 1, range(10)))

for t in range(k):
    print(['%.2f' % i for i in x])
    x = add(x, -1 * gamma(t) * g(x))


