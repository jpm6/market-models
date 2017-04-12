import numpy as np

la = np.linalg

'''
Objective Function => minimize sum(||Ai * x + bi||^2) for Ai,bi in A,b 
'''

# Dimensions
m = 4
n = 4

# Generate Random A Matrix and b Vector
A = np.random.random((m,n))
b = np.random.random((m,1))

# Or Load Given Instances
#A = np.loadtxt(open("problems/matrix_A.csv", "rb"))
#b = np.loadtxt(open("problems/vector_b.csv", "rb")).reshape(m,1)

# Function
f = lambda x: sum([(np.dot(A[i], x) ** 2 - b[i]) for i in range(m)])

# Probability Lookup
aiTai = [np.dot(np.transpose(row), row) for row in A]
probabilities = [i / sum(aiTai) for i in aiTai]

# Lipschitz Constant (TODO: Implement Power Iteration)
L = max(la.eig(2 * np.dot(np.transpose(A),A))[0])

# Step Size Gamma
gamma = 1 / L

# Start at Origin 
x = np.zeros((n,1))

# Iterations
k = 10

# Gradient Descent
for t in range(k):
    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", f(x))
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])

    # Random Selection
    r = np.random.choice(range(m), p = probabilities)

    # x = x - gamma * g(x)
    x = x - 2 * aiTai[r] * (np.dot(A[r], x) + b[r]) * A[r].reshape(m,1)
