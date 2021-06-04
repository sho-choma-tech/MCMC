import numpy as np 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('../data/toothgrowth.csv')

x = df.len
y = df.supp 

sd = np.std(x)

# Orange Juice の合計とサンプル数
n1 = np.sum(y == 'OJ')
x1 = df.query('supp == "OJ"').len  
mu1 = np.sum(x1) / (1 + n1)
sd1 = sd * np.sqrt(1 + np.sum(y=='OJ'))

# Vitamin C の合計とサンプル数
n2 = np.sum(y == 'VC')
x2 = df.query('supp == "OJ"').len
mu2 = np.sum(x2) / (1 + n2)
sd2 = sd * np.sqrt(1 + np.sum(y == "VC"))

# model pestririor probability of model mu1=mu0
q =  1 / (1 + np.sqrt(1+n1+n2) / ((1+n1) * (1+n2)) * np.exp(-(sum(x**2) / (1+n1+n2) - sum(x1**2) / (1+n1) - sum(x2**2) / (1+n2) ) /(2*sd**2)))

# BayesFactor
ans = np.log((q/(1-q)))
print(ans)