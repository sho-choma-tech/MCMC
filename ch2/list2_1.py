import numpy as np 
import random

import matplotlib.pyplot as plt 
import seaborn as sns 

## list 2.1 ##
random.seed(1)
a = np.random.uniform(1,0,3)

data_ = np.random.rand(100, 1)
plt.figure(figsize=(8,8))
plt.hist(data_, bins=50)
plt.show()

## 一様擬似乱数を1000個生成して、ヒストグラムにすると一様分布の確率密度関数と似ている
# 一様分布に従う独立な乱数 → 空間で一様に配置される（スペクトル検定）
