import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import beta 

def qbeta(p, shape1, shape2):    
    """
    Calculates the cumulative of the Beta-distribution
    """    
    result = beta.ppf(q=p, a=shape1, b=shape2, loc=0, scale=1)
    
    return result

def pbeta(q, shape1, shape2):
    result = beta.cdf(x=q, a=shape1, b=shape2, loc=0, scale=1)
    return result
    

c = list((qbeta(0.025, shape1=110313, shape2=105288), qbeta(0.975, shape1=110313, shape2=105288)))
mean_ = pbeta(0.5, shape1=110313, shape2=105288)
print(c)
print(mean_)