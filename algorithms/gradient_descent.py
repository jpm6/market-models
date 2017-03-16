import numpy as np

la = np.linalg

'''
Objective Function => minimize ||Ax - b||^2
'''
__author__ = "James P. Moriarty"

# Dimensions
m = 10
n = 10

# Generate Random A Matrix and b Vector
A = np.random.randint(-10, 10, (m,n))
b = np.random.randint(-10, 10, (m,1))

# Or Load Given Instances
A = np.loadtxt(open("problems/matrix_A.csv", "rb"))
b = np.loadtxt(open("problems/vector_b.csv", "rb")).reshape(m,1)

# Function
f = lambda x: np.dot(A,x) - b

# Gradient Function
g = lambda x: 2 * np.dot(np.transpose(A), f(x))

# Lipschitz Constant (TODO: Implement Power Iteration)
L = max(la.eig(2 * np.dot(np.transpose(A),A))[0])

# Step Size Gamma
gamma = 1 / L

# Start at Origin 
x = np.zeros((n,1))

# Iterations
k = 100

# Gradient Descent
for t in range(k):
    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bstep:\t\b\b\b\b", ['%.3f' % i for i in -gamma * g(x)], '\n')

    x = x - gamma * g(x)
