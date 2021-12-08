import pandas as pd
import numpy as np

# Author: Raul Macedo Fuzita
# Date: 07/12/2021
# All rights reserved
def checkDF(dfname, df, types=None, size=0, negative=True):

  print(dfname+'\n')
  xsize = len(df.columns)
  ysize = len(df.values)
  issue = False

  if type(size) != tuple:
      size = (size, ysize) if size > 0 else (xsize, ysize)

  if (ysize != size[1]): # Check if rows size are valid
    issue = True
    print('❌ (Row size)')
  if (xsize != size[0]): # Check if columns size are valid
    issue = True
    print('❌ (Column size)')
  elif types == None:
    pass
  elif len(types) != xsize: # Check if type list has the same colhmn size
    issue = True
    print('❌ (Type list smaller than the data frame)')
  elif not [df.iloc[:, [i]].dtypes != types[i] for i in range(0, xsize)]: # Check if columns type are valid
    issue = True
    print('❌ (Column type)')
  if df.isnull().values.any(): # Check if there is any NaN value
    issue = True
    print('❌ (Missing Values)')
  if (not negative) & (df.iloc[:,-1:].values.any() < 0): # Check if there is any negative value
    issue = True
    print('❌ (Negative)')
  if not issue: # If there is no issue
    print('✅ (Healthy)')
  print('\n','-'*100+'\n', end='')
  return not issue