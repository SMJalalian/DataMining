import pandas as pd
from Packages.LearningModel import ReplaceClassifier 

allInformation =  pd.read_csv("/Datasets/Diabetes_Diagnosis.csv")
allInformation.diabetes = allInformation.diabetes.apply(ReplaceClassifier)

for column in allInformation:
    if column != "diabetes":
        print("***********************************************")
        print("Segmentation of : ",column)
        List = allInformation[column]
        result = pd.cut(List,4)
        print(result)

