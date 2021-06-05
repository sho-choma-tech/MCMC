import numpy as np 
import pandas as pd 
import random


## list 2.4 ##
random.seed(1)
x_ = np.zeros(3*1000)

y = 1234

n = 2^31 -1
a = 65539
b = 0 

for i in np.arange(1, len(x_)):
    y = (a * y + b) % n
    x_[i] = y / n

x_mat = x_.reshape(1000, 3)
x_mat_frame = pd.DataFrame(x_mat)
print(x_mat_frame)