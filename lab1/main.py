import random
import sys
import math
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def first_func_one(lm, x):
    return 1 - np.e ** (-lm * x)

def second_func_one(a, b, x):
    return stats.norm.cdf((x - a)/b) - 0.5

def first_func(lm):
    e_arr = np.random.uniform(size=(10000))
    expo = pd.DataFrame()
    x = (-1/lm) * np.log(e_arr)
    expo[str(lm)] = x
    return expo

def second_func(a, b):
    e_arr = np.random.uniform(size=(10000, 12))
    normal = pd.DataFrame()
    mus = np.sum(e_arr, axis=1) - 6
    x = b * mus + a
    normal[str(a + b)] = x
    return normal

def third_alt(a, c):
    congr = pd.DataFrame()
    z_i = 11
    n_generated = []
    for i in range(10000):
        x_i = z_i / c
        z_i = (a*z_i) % c
        n_generated.append(x_i)
    congr[str(a + c)] = n_generated
    return congr

def ksi_first(lm):
    expo = first_func(lm)
    print('M:', expo.mean())
    print('D:', expo.std() **2)
    expo_stats = pd.DataFrame(
        expo[str(lm)]
    ).assign(Bin=lambda x: pd.cut(x[str(lm)], bins=20)
            ).groupby(['Bin']
                     ).agg({str(lm): ['count']})
    expo_stats.columns = ['count']
    expo_stats = expo_stats.reset_index()
    expo_stats['expected'] = expo_stats['Bin'].apply(
        lambda x: first_func_one(lm, x.right) - first_func_one(lm, x.left)
    ).astype(float)*10000
    ksi2 = (((expo_stats['count'] - expo_stats['expected']) ** 2) / expo_stats['expected']).sum()
    print('Lambda:', lm, '; ksi2: ', ksi2)
    print('Critical {}'.format(stats.chi2.ppf(q = 0.95, df = 18) ))
    expo.hist(bins=20, figsize=(15, 10))
    plt.show()

def ksi_second(a, b):
    normal = second_func(a, b)
    print('M:', normal.mean())
    print('D:', normal.std() **2)
    normal_stats = pd.DataFrame(
        normal[str(a + b)]
    ).assign(Bin=lambda x: pd.cut(x[str(a + b)], bins=20)
            ).groupby(['Bin']
                     ).agg({str(a + b): ['count']})
    normal_stats.columns = ['count']
    normal_stats = normal_stats.reset_index()
    normal_stats['expected'] = normal_stats['Bin'].apply(
        lambda x: second_func_one(a, b, x.right) - second_func_one(a, b, x.left)
    ).astype(float)*10000
    ksi2 = (((normal_stats['count'] - normal_stats['expected']) ** 2) / normal_stats['expected']).sum()
    print('a:', a, 'b:', b, ' ksi2: ', ksi2)
    print('Critical {}'.format(stats.chi2.ppf(q = 0.95, df = 17)))
    normal.hist(bins=20, figsize=(15, 10))
    plt.show()

def ksi_third(a, b):
    congr = third_alt(a, b)
    print('M:', congr.mean())
    print('D:', congr.std())
    df_unif_stats = pd.DataFrame(
        congr[str(a + b)]
    ).assign(Bin=lambda x: pd.cut(x[str(a + b)], bins=7)
            ).groupby(['Bin']
                     ).agg({str(a + b): ['count']})
    df_unif_stats.columns = ['count']
    df_unif_stats = df_unif_stats.reset_index()
    df_unif_stats['expected'] = 10000/7
    ksi2 = (((df_unif_stats['count'] - df_unif_stats['expected']) ** 2) / df_unif_stats['expected']).sum()
    print('a:', congr[str(a + b)].min(), 'b:', congr[str(a + b)].max(), ' ksi2: ', ksi2)
    print('Critical {}'.format(stats.chi2.ppf(q = 0.95, df = 17)))
    congr.hist(bins=7, figsize=(15, 10))
    plt.show()

dataset_first = [0.5, 1, 1.5]
dataset_second = [(0, 1), (0, 6), (2, 4)]
dataset_third = [(5**13, 2**31), (5**7, 2**13), (5**7, 2**12)]

plot = sys.argv[1]
dataset = sys.argv[2]
plot = int(plot)
dataset = int(dataset)
if plot is 1:
    ksi_first(dataset_first[dataset - 1])
if plot is 2:
    a, b = dataset_second[dataset - 1]
    ksi_second(a, b)
if plot is 3:
    a, b = dataset_third[dataset - 1]
    ksi_third(a, b)


