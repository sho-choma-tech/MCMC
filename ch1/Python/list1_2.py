import numpy as np 
import numpy.matlib
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

color_ = np.array([[0,0,0,1,1,1], [0,1,0,1,0,1]])
card_ = np.random.multinomial(n=10000, size=1, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
r_ = np.sum(card_*color_[0])
rr_ = np.sum(card_*color_[0]*color_[1])

ans = rr_ / r_

print(ans)
