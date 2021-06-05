import numpy as np 
import random
from scipy import stats
from scipy.stats import kstest, uniform 


random.seed(10)
u = np.random.uniform(1,0,1000)
ans = kstest(u, uniform.cdf)

print(ans)

'''
p値は小さくないので、統計的基準として一様擬似乱数は一様分布からの独立な乱数列として差はない

'''