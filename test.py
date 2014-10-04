__author__ = 'andrewa'
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

X = np.loadtxt('diabetes.data', skiprows=1)

y = X[:, -1]
X = X[:, 0:-1]

ytrain, ytest = y[0:200], y[200:422]
Xtrain, Xtest = X[0:200], X[200:422]

Xbar = np.mean(Xtrain, axis=0) # среднее
Xstd = np.std(Xtrain, axis=0) # отклонение от среднего
ybar = np.mean(ytrain) # среднее
ytrain = ytrain - ybar
Xtrain = (Xtrain - Xbar) / Xstd # нормирование


alphas = [i for i in xrange(1, 10000)]
clf = Ridge(fit_intercept=False)

coefs = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(Xtrain, ytrain)
    coefs.append(clf.coef_)


ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Ridge  with regulization')
plt.show()