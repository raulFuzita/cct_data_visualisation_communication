import pandas as pd
import numpy as np

# Author: Raul Macedo Fuzita
# Date: 01/12/2021
# All rights reserved
def pivot_melt(data, column, value, fill=0, filter=None):
  if (type(filter) is list) | (type(filter) is np.ndarray) & (len(filter) > 0):
    data = data[np.isin(data, filter)]
  colnames = data.loc[:,column].unique()
  newdf = pd.DataFrame()
  for name in colnames:
    col = data[data[column] == name][value]
    temp = pd.DataFrame({name:col.values})
    newdf = pd.concat([newdf, temp], axis=1)
  newdf.fillna(fill, inplace=True)
  return newdf