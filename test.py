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
error = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(Xtrain, ytrain)
    coefs.append(clf.coef_)
    C = np.array(clf.coef_)
    E = np.dot(ytrain - np.dot(Xtrain, C).transpose(), ytrain - np.dot(Xtrain, C))
    error.append(E)
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Ridge  with regulization')
plt.show()

Plote = []
Plote.append(error[:100]) #график ошибки тренир

Xbar = np.mean(Xtest, axis=0) # среднее
Xstd = np.std(Xtest, axis=0) # отклонение от среднего
ybar = np.mean(ytest) # среднее
ytest = ytest - ybar
Xtest = (Xtest - Xbar) / Xstd # нормирование


alphas = [i for i in xrange(1, 10000)]
clf = Ridge(fit_intercept=False)

coefs = []
error = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(Xtest, ytest)
    coefs.append(clf.coef_)
    C = np.array(clf.coef_)
    E = np.dot(ytest - np.dot(Xtest, C).transpose(), ytest - np.dot(Xtest, C))
    error.append(E)


Plote.append(error[:100]) # график ошибки тестов
ax = plt.gca()
ax.plot(alphas[:100], Plote[0])
ax.plot(alphas[:100], Plote[1])
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Error')
plt.show()