import numpy as np


def standardization(X):
    '''数据的归一化'''

    m, n= X.shape
    for j in range(n):
        mean = np.mean(X[:,j])
        std = np.std(X[:,j])
        for i in range(m):
            if std==0:
                X[i, j]=0
            else:
                X[i, j] = (X[i, j]-mean)/std
    return X



