# encoding: utf-8
#

import sklearn.datasets
import numpy as np
from action.linear.perceptron import Perceptron
from action.linear.adalineGD import AdalineGD
import pandas as pd

iris = sklearn.datasets.load_iris()
X = iris.data
y = iris.target
df1 = pd.DataFrame(X)
df2 = pd.DataFrame(y)
df = pd.concat([df1, df2], axis=1)
size = X.shape[0]
X_train, y_train = df.iloc[:100, [0,2]].values, df.iloc[:100, 4].values
y_train = np.where(y_train == 0, -1, 1)


def test_perceptron(X_train, y_train):
    p = Perceptron()
    p.fit(X_train, y_train)
    # print("train ", X_train.shape, "test ", X_test.shape)
    print(p.error_)


test_perceptron(X_train, y_train)


def test_adaline(X_train, y_train):
    ad = AdalineGD(eta=0.01)
    X_train = (X_train - X_train.mean())/X_train.std()
    ad.fit(X_train, y_train)
    print(ad.cost_)

# test_adaline(X_train, y_train)
