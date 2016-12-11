import pandas as pd
import numpy as np

df = pd.read_csv('train.csv', header=0)

print df.tail(3)

df.info()