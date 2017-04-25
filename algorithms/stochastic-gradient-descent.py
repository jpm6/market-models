import numpy  as np
import pandas as pd

la = np.linalg

'''
Objective Function => minimize vi |wT*ui + b||^2
'''

trd = '../data/split/train-data.csv'
trl = '../data/split/train-labels.csv'

d = np.asarray(pd.read_csv(trd))
l = np.asarray(pd.read_csv(trl))

# Gram Matrix
m, n = d.shape
K = np.zeros((m,m))

for i, x_i in enumerate(d):
    for j, x_j in enumerate(d):
        K[i, j] = np.inner(x_i, x_j)
# Lipschitz Constant (TODO: Implement Power Iteration)
# L = max(la.eig(2 * np.dot(np.transpose(A),A))[0])

# Step Size Gamma
# gamma = 1 / L

# Start at Origin 
x = np.ones(n)

# Stochastic Gradient Descent
for u,v in list(zip(d,l))[:10]:

 #   G = 

    '''
    print("\t\b\b\bx:\t\t\b\b\b\b", ['%.3f' % i for i in x])
    print("\t\b\b\bu:\t\t\b\b\b\b", ['%.3f' % i for i in u])
    print('',t, "\t\b\b\bf(x):\t\b\b\b\b", la.norm(f(x)) ** 2)
    print("\t\b\b\bstep:\t\b\b\b\b", ['%.3f' % i for i in -gamma * g(x)], '\n')
    '''

    print(v[0], np.dot(x, u))
    h = v[0] * np.dot(x, u)
    print(h)
    #x = x - gamma * g(x)
    x = x - 0.001 * h * u


ted = '../data/split/test-data.csv'
tel = '../data/split/test-labels.csv'

d = np.asarray(pd.read_csv(ted))
l = np.asarray(pd.read_csv(tel))

for u,v in list(zip(d,l)):
    pass
    
