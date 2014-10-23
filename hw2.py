__author__ = 'andrewa'
#-*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
from time import sleep
words = open('data/vocabulary.txt', 'r').read().split('\n')
newsgroup_names = open('data/newsgrouplabels.txt', 'r').read().split('\n')
labels_train = np.loadtxt('data/train.label', skiprows=1)
labels_test = np.loadtxt('data/test.label', skiprows=1)
data_train = np.loadtxt('data/train.data')
data_test = np.loadtxt('data/test.data', skiprows=1)
data_train_doc_id = data_train[:, 0]
data_train_word_id = data_train[:, 1]
data_train_count = data_train[:, 2]
alph = 1.0/len(words)

p_X_giv_Y = np.zeros((len(newsgroup_names)+1, len(data_train_word_id)), dtype=np.float)
pY = np.zeros((len(newsgroup_names)+1, 1), dtype=np.float)

for i in xrange(1, len(newsgroup_names)+1):
    pY[i] = np.size(labels_train[np.where(labels_train == i)])
#вероятность темы
pY_prob = np.divide(pY, sum(pY))

for i in xrange(1, len(data_train)):
    try:
        p_X_giv_Y[labels_train[data_train_doc_id[i-1]-1], data_train_word_id[i-1]] += data_train_count[i-1]
    except:
        pass
p_X_giv_Y_prob = p_X_giv_Y
#вероятность слова относительно темы
for i in xrange(1, len(newsgroup_names)+1):
    p_X_giv_Y_prob[i, :] = np.divide(p_X_giv_Y[i, :], sum(p_X_giv_Y[i, :]))

TEST = np.zeros((len(newsgroup_names)+1, len(data_train_doc_id)), dtype=np.float)

for i in xrange(0, len(data_train_doc_id)):
    for j in xrange(1, len(newsgroup_names)+1):
        TEST[j, i] += math.log(pY_prob[j])
print TEST

for i in xrange(0, len(data_train)):
    for j in xrange(1, len(newsgroup_names)+1):
        TEST[j, data_train_doc_id[i]] = TEST[j, data_train_doc_id[i]] + data_train_count[j] * math.log((p_X_giv_Y_prob[j,data_train_word_id[i]])+1)/(len(data_train_word_id)+sum(p_X_giv_Y[j, :]))

print TEST

