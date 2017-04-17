import numpy as np
import matplotlib.pyplot as plt

la = np.linalg

'''
Objective Function => minimize ||Ax - b||^2
'''

# Dimensions
m = 10
n = 10

# Generate Random c Matrix
c = np.random.randint(-10, 10, n)

# J = j of max |c_j| in Matrix c 
J = lambda i: np.argmax(abs(i))

y = np.array([int(i == J(c)) for i in range(n)])

if c[J(c)] >= 0: y *= -1

# Load Given Instances
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

# Store Each Iteration for Plots
fxs = []

# Gradient Descent
for t in range(1,k+1):

    gamma = 2 / (t + 2)

    fxs.append(la.norm(f(x)) ** 2)

    c = g(x)
    s = np.array([int(i == J(c)) for i in range(n)]).reshape(n,1)
    
    if c[J(c)] >= 0: s *= -1

    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bstep:\t\b\b\b\b", ['%.3f' % i for i in gamma*( s-x)], '\n')

    x = x + gamma * (s - x)


plt.plot(fxs)
plt.title('Constrained Gradient Descent with Frank-Wolfe')
plt.xlabel('Iteration')
plt.ylabel('f(x)')
plt.show()

