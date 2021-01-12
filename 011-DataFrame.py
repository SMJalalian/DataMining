import numpy as np
import pandas as pd
import os
from Packages.MathHelper import IG_Entropy

def clear(): os.system( 'cls' )
df = pd.read_csv("DetaFruit.csv")
print(df.head())
print(df.describe())

Melon = Orange = Apple = 0
Total = len(df)

for i,row in df.iterrows():
    if row['class'] =='melon' :
        Melon += 1
    elif row['class'] =='orange' :
        Orange += 1
    elif row['class'] =='apple' :
        Apple += 1

All_Entropy = IG_Entropy(Melon/Total, Orange/Total, Apple/Total)
print('Dataset Entropy: %.3f bits' % All_Entropy)
