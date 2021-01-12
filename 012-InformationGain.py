import numpy as np
import pandas as pd
from Packages.MathHelper import IG_Entropy

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
#
#c1_class0 = 0
#c1_class1 = 0
#c1_class2 = 0
#
##total number of fruits
#total = len(df)
#conditionVaue = 499
#attrib = 'attr2'
#
#for i,row in df.iterrows():
#    if row['class'] =='melon' and row[attrib] < conditionVaue :
#        c1_class0 = c1_class0 + 1
#    elif row['class'] =='orange' and row[attrib] < conditionVaue:
#        c1_class1 = c1_class1 + 1
#    elif row['class'] =='apple'  and row[attrib] < conditionVaue:
#        c1_class2 = c1_class2 + 1
#c1_total = c1_class0 + c1_class1 + c1_class2
#c1_entropy = entropy(c1_class0/c1_total , c1_class1/c1_total , c1_class2/c1_total )
#
#
#dc1_class0 = 0
#dc1_class1 = 0
#dc1_class2 = 0
#
#
#for i,row in df.iterrows():
#    if row['class'] =='melon' and row[attrib] >= conditionVaue :
#        dc1_class0 = dc1_class0 + 1
#    elif row['class'] =='orange' and row[attrib] >= conditionVaue:
#        dc1_class1 = dc1_class1 + 1
#    elif row['class'] =='apple'  and row[attrib] >= conditionVaue:
#        dc1_class2 = dc1_class2 + 1
#dc1_total = dc1_class0 + dc1_class1 + dc1_class2
#dc1_entropy = entropy(dc1_class0/dc1_total , dc1_class1/dc1_total , dc1_class2/dc1_total )
#
#conditionEntropy = (c1_total / total) * c1_entropy + (dc1_total/total) * dc1_entropy
#print('Condition Entropy: %.3f bits' % conditionEntropy)
#
#gain = s_entropy - conditionEntropy
#print('Information Gain: %.3f bits' % gain)





