import numpy as np
import pandas as pd
from Packages.MathHelper import IG_Entropy
import os
def clear(): os.system( 'cls' )

def CheckTotalEntropy (dataFrame) :
    Melon = Orange = Apple = 0
    Total = len(dataFrame)
    for i,row in df.iterrows():
        if row['class'] =='melon' :
            Melon += 1
        elif row['class'] =='orange' :
            Orange += 1
        elif row['class'] =='apple' :
            Apple += 1
    return IG_Entropy(Melon/Total, Orange/Total, Apple/Total)   
#*******************************************************************     
def CheckConditionalEntropy ( dataFrame ,attrib , conditionValue ):
    
    Total = len(dataFrame)

    C_Melon = C_Orange = C_Apple = 0
    for i,row in dataFrame.iterrows():
        if row['class'] =='melon' and row[attrib] < conditionValue :
            C_Melon += 1
        elif row['class'] =='orange' and row[attrib] < conditionValue :
            C_Orange += 1
        elif row['class'] =='apple' and row[attrib] < conditionValue :
            C_Apple += 1
    C_Total = C_Melon + C_Orange + C_Apple
    C_Entropy = IG_Entropy(C_Melon/C_Total, C_Orange/C_Total, C_Apple/C_Total)

    Duality_Melon = Duality_Orange = Duality_Apple = 0
    for i,row in dataFrame.iterrows():
        if row['class'] =='melon' and row[attrib] >= conditionValue :
            Duality_Melon += 1
        elif row['class'] =='orange' and row[attrib] >= conditionValue :
            Duality_Orange += 1
        elif row['class'] =='apple' and row[attrib] >= conditionValue :
            Duality_Apple += 1
    Duality_Total = Duality_Melon + Duality_Orange + Duality_Apple
    Duality_Entropy = IG_Entropy(Duality_Melon/Duality_Total, Duality_Orange/Duality_Total, Duality_Apple/Duality_Total)

    Condition_Entropy = (( C_Total / Total) * C_Entropy ) + ((Duality_Total / Total) * Duality_Entropy)
    return Condition_Entropy
#******************************************************
df = pd.read_csv("DetaFruit.csv")
All_Attribs = ["attr1","attr2","attr3"]
TOTAL_ENTROPY = CheckTotalEntropy(df)

for attr in All_Attribs:
    des = df[attr].describe()
    min = int(des["min"]) + 1
    max = int(des["max"]) - 1
    iteration = max - min
    minimumEnropy = 0
    minimumIG = 0
    MinEntropyCondition = 0
    MinIGCondition = 0
    firstLoop = True
    for i in range(iteration):
        currentEntropy = CheckConditionalEntropy(df, attr , min)
        currentIG = TOTAL_ENTROPY - currentEntropy
        if firstLoop == True:
            MinEntropyCondition = min
            MinIGCondition = min
            minimumEnropy = currentEntropy
            minimumIG = currentIG
            firstLoop = False
        else:
            if currentEntropy < minimumEnropy:
                minimumEnropy = currentEntropy
                MinEntropyCondition = min
            if currentIG < MinIGCondition :
                minimumIG = currentIG
                MinIGCondition = min              
        min += 1
    print("****************************************")
    print("Information about ",attr)
    print("Minimum Entropy = " , minimumEnropy)
    print("Selected Condition: " , MinEntropyCondition)
    print("Minimum IG = " , minimumIG)
    print("Selected Condition for IG: " , MinIGCondition)



