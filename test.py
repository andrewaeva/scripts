__author__ = 'andrewa'
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

X = np.loadtxt('diabetes.data', skiprows=1)

y = X[:, -1]
X = X[:, 0:-1]

ytrain_0, ytest_0 = y[0:220], y[220+1:442+1]
Xtrain, Xtest = X[0:220], X[220+1:442+1]

Xbar = np.mean(Xtrain, axis=0) # среднее
Xstd = np.std(Xtrain, axis=0) # отклонение от среднего
ybar = np.mean(ytrain_0) # среднее
ytrain = ytrain_0 - ybar
Xtrain = (Xtrain - Xbar) / Xstd # нормирование

alphas = [i for i in xrange(0, 10000)]
clf = Ridge(fit_intercept=False)

Plote = []

coefs = []
error = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(Xtrain, ytrain)
    coefs.append(clf.coef_)
    C = np.array(clf.coef_)
    E = np.linalg.norm(ytrain - np.dot(Xtrain, C)) / np.linalg.norm(ytrain)
    error.append(E)

Plote.append(error)

ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Ridge  with regulization')
plt.show()

Xtest = (Xtest - Xbar) / Xstd # нормирование

error = []
for a in alphas:
    E = np.linalg.norm(ytest_0 - ybar - np.dot(Xtest, coefs[a])) / np.linalg.norm(ytrain)
    error.append(E)

Plote.append(error) # график ошибки тестов

ax = plt.gca()
ax.plot(alphas, Plote[0])
ax.plot(alphas, Plote[1])
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Error')
plt.show()

##############################################
#cross validations
##############################################
X = np.loadtxt('diabetes.data', skiprows=1)

y = X[:, -1]
X = X[:, 0:-1]

ytrain_0, ytest_0 = y[0:100], y[100:440]
Xtrain, Xtest = X[0:100], X[100:440]

Xbar = np.mean(Xtrain, axis=0) # среднее
Xstd = np.std(Xtrain, axis=0) # отклонение от среднего
ybar = np.mean(ytrain_0) # среднее
ytrain = ytrain_0 - ybar
Xtrain = (Xtrain - Xbar) / Xstd # нормирование

alphas = [i for i in xrange(0, 10000)]
clf = Ridge(fit_intercept=False)

Plote = []

coefs = []
error = []
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(Xtrain, ytrain)
    coefs.append(clf.coef_)
    C = np.array(clf.coef_)
    E = np.linalg.norm(ytrain - np.dot(Xtrain, C)) / np.linalg.norm(ytrain)
    error.append(E)

Plote.append(error)

ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Ridge  with regulization')
plt.show()

Xtest = (Xtest - Xbar) / Xstd # нормирование

error = []
for a in alphas:
    E = np.linalg.norm(ytest_0 - ybar - np.dot(Xtest, coefs[a])) / np.linalg.norm(ytrain)
    error.append(E)

Plote.append(error) # график ошибки тестов

ax = plt.gca()
ax.plot(alphas, Plote[0])
ax.plot(alphas, Plote[1])
ax.set_xscale('log')
plt.xlabel('lambda')
plt.title('Error')
plt.show()
