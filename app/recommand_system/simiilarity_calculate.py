import pandas as pd
from math import sqrt
import numpy as np

def pd_length(*args):
    sum = 0.0
    print('===='*40)
    # if len(args) == 0:
    for i in range(len(args[0])):
        sum += pow(args[0][i], 2)
        pass
    # else:
    #     for i in range(len(args)-1):
    #         for j in range(len(args[i][j])):
    #             temp = args[i][j] - args[i+1][j]
    #             sum += pow(temp, 2)
    sum = sqrt(sum)
    return sum

def self_distance_similarity(matrix):
    for i in range(len(matrix)-1):
        lenght = 0
        lenght = pd_length(matrix[i], matrix[i+1])
    pass

def self_cos_similarity(matrix):
    df = pd.DataFrame(matrix)
    for i in range(len(matrix)):
        s = pd.Series(matrix[i])
        #print(s)
        product = pd_length(matrix[i]) * pd_length(s)
        print(' dot product: {} '.format(df.dot(s)))
        degree = np.arccos(df.dot(s).div(product))
        print(' degree: {} '.format(degree))
    pass