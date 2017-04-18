import numpy as np
import matplotlib.pyplot as plt

la = np.linalg

'''
Objective Function => minimize ||Ax - b||^2
'''

# Dimensions
m = 10
n = 10


# Load Given Instances
A = np.loadtxt(open("matrix_A.csv", "rb"))
b = np.loadtxt(open("vector_b.csv", "rb")).reshape(m,1)

# Function
f = lambda x: np.dot(A,x) - b

# Gradient Function
g = lambda x: 2 * np.dot(np.transpose(A), f(x))

# Lipschitz Constant (TODO: Implement Power Iteration)
L = max(la.eig(2 * np.dot(np.transpose(A),A))[0])

# Step Size Gamma
gamma = 1 / L

# Start at Origin 
x = np.ones((n,1))

# Iterations
k = 100

j = lambda i: np.argmax(abs(i))
functionvals = []

# Gradient Descent
for t in range(1,k+1):

    gamma = 2 / (t + 1)

    functionvals.append(la.norm(f(x)) ** 2)

    C = g(x)
    result = np.array([int(j(C)==i) for i in range(10)]).reshape(n,1)
    if C[j(C)] >= 0:
        result *= -1

    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bstep:\t\b\b\b\b", ['%.3f' % i for i in gamma*(result-x)],'\n')

    x = x + gamma * (result - x)

plt.plot(functionvals)
plt.xlabel('Iters')
plt.ylabel('Func Vals')
plt.title('Problem 3 Plot')
plt.show()

