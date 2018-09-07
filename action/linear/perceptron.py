# encoding: utf-8
#

import numpy as np


class Perceptron():
    def __init__(self, eta=0.1, n_iter=50, random_state=0):
        self.eta = eta
        self.n_inter = n_iter
        self.random_state = random_state


    """
    y  integer
    update is calculate by xi
    """
    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1] + 1)
        self.error_ = []
        for i in range(self.n_inter):
            error = 0
            for xi, yi in zip(X, y):
                update = self.eta * (yi - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                error += int(update != 0.0)
            self.error_.append(error)
        pass


    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]


    def predict(self, X):
        return np.where(self.net_input(X) >= 0, 1, -1)


    if __name__ == "__main__":
        p = Perceptron()
        import sklearn.datasets

        iris = sklearn.datasets.load_iris()
        X = iris.data
        y = iris.target
        size = X.shape[0]
        slice = int(size * 0.8)
        X_train, y_train = X[:100], y[:100]
        y_train = np.where(y_train == 0, -1, 1)
        print(y_train)
        p.fit(X_train, y_train)
        # print("train ", X_train.shape, "test ", X_test.shape)
        print(p.error_)
        print(y)
