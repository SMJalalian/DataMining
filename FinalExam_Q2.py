import pandas as pd
from Packages.LearningModel import ReplaceClassifier 

allInformation =  pd.read_csv("/Datasets/Diabetes_Diagnosis.csv")
allInformation.diabetes = allInformation.diabetes.apply(ReplaceClassifier)

#*********************     Question 2     *************************
# Descriptive statistics male
statistics_Diabeties = allInformation[allInformation['diabetes'] == '1'].describe()
statistics_Diabeties.rename(columns=lambda x: x + '_1', inplace=True)

# Descriptive statistics female
statistics_NonDiabeties = allInformation[allInformation['diabetes'] == '0'].describe()
statistics_NonDiabeties.rename(columns=lambda x: x + '_0', inplace=True)

# Dataframe that contains statistics for both male and female
statistics = pd.concat([statistics_Diabeties, statistics_NonDiabeties], axis=1)
statistics
statistics.to_csv('Exports/RegressionResult.csv')