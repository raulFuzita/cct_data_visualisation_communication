import pandas as pd
import numpy as np

def mmnorm(col):
  return (col - col.min()) / (col.max() - col.min())