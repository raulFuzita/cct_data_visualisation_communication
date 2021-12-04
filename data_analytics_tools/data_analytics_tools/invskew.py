import pandas as pd
import numpy as np
import statistics as sts

def invskew(col):
  return (3*(np.mean(col) - sts.median(col))) / np.std(col)