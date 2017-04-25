from sklearn.linear_model import SGDClassifier

import numpy  as np
import pandas as pd

trd = '../data/split/train-data.csv'
trl = '../data/split/train-labels.csv'

X = np.asarray(pd.read_csv(trd))
y = np.asarray(pd.read_csv(trl)).reshape(295,)

clf = SGDClassifier(loss="hinge", penalty="l2")
clf.fit(X, y)

ted = '../data/split/test-data.csv'
tel = '../data/split/test-labels.csv'

d = np.asmatrix(pd.read_csv(ted))
l = np.asarray(pd.read_csv(tel))

c = 0

for u,v in list(zip(d,l)):
    if clf.predict(u) == v: c += 1 
