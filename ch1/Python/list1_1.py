from matplotlib.pyplot import table
import numpy as np 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
from plotnine.data import diamonds

# Variables groups 
cut_vars = ['cut', 'color', 'clarity']
xvars = cut_vars + ['carat']
all_vars = xvars + ['price']

df = diamonds.copy()

df_color = df[['cut', 'color', 'x']].pivot_table(index='cut', columns='color', aggfunc='count')

print(df.head())
print('-----------------------------------------------------------------------------------')
print(df_color)

