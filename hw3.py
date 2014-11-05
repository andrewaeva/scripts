#-*-coding:utf-8-*-
from __future__ import division
__author__ = 'andrewa'
import numpy as np
import math
import matplotlib.pyplot as plt


def logistic(a):
    return 1.0 / (1 + np.exp(-a))


def irls(X, y):
    alpha = 0.001
    theta = np.zeros(X.shape[1])
    theta_ = np.inf
    #while max(abs(theta - theta_)) > 1e-6:
    for i in xrange(0, 20):
        a = np.dot(X, theta)
        pi = logistic(a)
        SX = X * (pi - pi*pi).reshape(-1, 1)
        XSX = np.dot(X.T, SX) + np.multiply(alpha, np.eye(np.size(theta, 0)))
        SXtheta = np.dot(SX, theta)
        theta_ = theta
        theta = np.linalg.solve(XSX, np.dot(X.T, SXtheta + y - pi) + alpha * theta)
    return theta

train = np.loadtxt('HW3_data/train.csv', delimiter=',')
train_labels = np.loadtxt('HW3_data/train_labels.txt')
test = np.loadtxt('HW3_data/test.csv', delimiter=',')
test_labels = np.loadtxt('HW3_data/test_labels.txt')
size_doc = np.size(train, 0)
size_word = np.size(train, 1)
size_doc_test = np.size(test, 0)
size_word_test = np.size(test, 1)
theme_one = np.size(np.where(train_labels == 1), 0)
theme_zero = np.size(np.where(train_labels == 0), 0)


###########################################################
print('IRLS')
###########################################################

theta = irls(train, train_labels)
###########################################################
#
###########################################################
z_test = logistic(test*theta)
label_test = np.zeros((size_doc_test, 2))
label_test[:, 0] = test_labels
for i in xrange(0, size_doc_test):
        if z_test[i, 0] >= 0.5:
            label_test[i, 1] = 1
        else:
            label_test[i, 1] = 0
answer_test = 0
for i in label_test:
    if i[0] == i[1]:
        answer_test += 1
print answer_test, answer_test/size_doc
###########################################################
#                   ЧИТЕРНЫЙ КОД
###########################################################
#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.metrics import classification_report
#clf = GradientBoostingClassifier()
#clf.fit(train, train_labels)
#y_pred = clf.predict(test)
#print classification_report(test_labels, y_pred,
#                            target_names=['0','1'])

###########################################################
print('Логистическая регрессия Градиентный спуск без регуляризации')
###########################################################
alpha = 0.001
max_itr = 400
theta = np.zeros((size_word, 1))

label = np.zeros((size_doc, 2))
label[:, 0] = train_labels
answer = np.zeros((max_itr, 1))

for count in xrange(0, max_itr):
    print 'lol'
    z = logistic(np.dot(train, theta))
    for i in xrange(0, size_doc):
        if z[i, 0] >= 0.5:
            label[i, 1] = 1
        else:
            label[i, 1] = 0
    for i in label:
        if i[0] == i[1]:
            answer[count] += 1

    if count <= 100:
        print(count, answer[count], size_doc, answer[count]/size_doc)
    theta = theta + np.multiply(alpha, (np.dot(train.transpose(), (label[:, 0] - z[:, 0]))))
    print(theta[0, 1])


z_test = logistic(test*theta)
label_test = np.zeros((size_doc_test, 2))
label_test[:, 0] = test_labels
for i in xrange(0, size_doc_test):
        if z_test[i, 0] >= 0.5:
            label_test[i, 1] = 1
        else:
            label_test[i, 1] = 0
answer_test = 0
for i in label_test:
    if i[0] == i[1]:
        answer_test += 1

print(answer_test)