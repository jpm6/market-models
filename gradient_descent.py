import numpy as np

la = np.linalg

'''
Objective Function => minimize ||Ax + b||^2
'''

# Instance Dimensions
d = 5

# Generate Random A Matrix and B Vector
A = np.random.randint(-10, 10, d * d).reshape(d,d)
b = np.random.randint(-10, 10, d).reshape(d,1)

# Function
f = lambda x: np.dot(A,x) + b

# Gradient Function
g = lambda x: np.dot(np.transpose(A), f(x))

# Iterations
k = 100

# Lipschitz Constant (TODO: Implement Power Iteration)
L = max(la.eig(np.dot(np.transpose(A),A))[0])

# Step Size Gamma
gamma = 1 / L

# Start at Origin 
x = np.zeros((d,1))

# Gradient Descent
for t in range(k):
    print('',t, "\t\b\b\bf(x):\t\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bx:\t\t\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bstep:\t\b\b\b", ['%.3f' % i for i in -gamma * g(x)], '\n')

    x = x - gamma * g(x)
