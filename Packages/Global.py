import hazm 
import pandas as pd
import matplotlib.pyplot as plt

def loadRawData(path):
    dataFrame = pd.read_excel(path)
    dataFrame = dataFrame[pd.notnull(dataFrame['comment'])]
    dataFrame = dataFrame.drop_duplicates()
    return dataFrame 

def loadLabledData(path):
    dataFrame = pd.read_csv(path)
    dataFrame = dataFrame[pd.notnull(dataFrame['Label'])]
    dataFrame = dataFrame[pd.notnull(dataFrame['comment'])]
    dataFrame = dataFrame.drop_duplicates()
    return dataFrame
#***************************************************
def EmojiInformation(sampleDataframe):
    fig = plt.figure(figsize=(8,6))
    sampleDataframe.groupby('Label').comment.count().sort_values().plot.bar(
    ylim=0, title= 'Term Frequency of each Emoji \n')
    plt.xlabel('\n Number of ocurrences', fontsize = 10);
    plt.show()
#***************************************************
def Load_Hazm_Normalization():
    normalizer =  hazm.Normalizer()
    tokenizer = hazm.SentenceTokenizer()
    tokens = hazm.word_tokenize 
    S_Words = list(hazm.stopwords_list())
    S_Words += ["ام","خد","y۳","y۵","۲۰۱۷","شدم",".","،","ست","…"]
    return normalizer, tokenizer, tokens, S_Words
#***************************************************
