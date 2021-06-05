import pandas as pd 
import numpy as np 
import random 

random.seed(1)
lambda_ = 2.0
u = np.random.uniform(1, 0, 3)
log_u = -(np.log10(u)) / lambda_

# print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")