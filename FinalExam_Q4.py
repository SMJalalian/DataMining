import pandas as pd
from Packages.LearningModel import ReplaceClassifier 

#Load Dataset
allInformation =  pd.read_csv("/Datasets/Diabetes_Diagnosis.csv")
allInformation.diabetes = allInformation.diabetes.apply(ReplaceClassifier)

#Perform Segmentation for each columns
for column in allInformation:
    if column != "diabetes":
        print("***********************************************")
        print("Segmentation of : ",column)
        List = allInformation[column]
        result = pd.cut(List,4)
        print(result)

