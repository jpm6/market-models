import numpy as np

la = np.linalg

'''
Objective Function => minimize ||Ax - b||^2
'''

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
eig_vals = la.eig(2 * np.dot(np.transpose(A),A))[0]

L = max(eig_vals)
u = min(eig_vals)

# Start at Origin 
x = xt = np.zeros((n,1))

# Iterations
k = 100

# Accelerated Gradient Descent
for t in range(1,k+1):
    alpha = 2 / (t + 1)
    gamma = t / (2 * L)
         
    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bstep:\t\b\b\b\b", ['%.3f' % i for i in -gamma * g(x)], '\n') 

    # X with bottom bar 
    xb = (1 - alpha) * xt + alpha * x
    
    # Update Step
    x = (x + gamma * (u * xb - g(xb))) / (u * gamma + 1) 

    # X with top bar 
    xt = (1 - alpha) * xt + alpha * x
