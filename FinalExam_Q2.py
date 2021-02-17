import pandas as pd
from Packages.LearningModel import ReplaceClassifier 

allInformation =  pd.read_csv("/Datasets/Diabetes_Diagnosis.csv")
allInformation.diabetes = allInformation.diabetes.apply(ReplaceClassifier)

#*********************     Question 2     *************************
# Descriptive statistics Diabetes
statistics_Diabetes = allInformation[allInformation['diabetes'] == '1'].describe()
statistics_Diabetes.rename(columns=lambda x: x + '_True', inplace=True)

# Descriptive statistics NonDiabetes
statistics_NonDiabetes = allInformation[allInformation['diabetes'] == '0'].describe()
statistics_NonDiabetes.rename(columns=lambda x: x + '_False', inplace=True)

# Dataframe that contains statistics for both Diabetes and NonDiabetes
statistics = pd.concat([statistics_Diabetes, statistics_NonDiabetes], axis=1)
statistics.to_csv('Exports/Q2_Regression_Result.csv')