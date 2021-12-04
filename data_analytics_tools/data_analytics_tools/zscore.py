import pandas as pd
import numpy as np

def zscore(col):
  return (col - col.mean()) / np.std(col)