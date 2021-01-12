import math
import numpy as np

def Entropy(textObject):
    ent = 0
    for word in textObject.UniqueWords :
        repeat = (list(textObject.AllWords)).count(word)
        temp = (repeat/textObject.AllWordsCount) * (math.log(repeat/textObject.AllWordsCount))
        ent += temp
    return math.fabs(ent)
#************************************************
def IG_Entropy(class0, class1,class2):

    Output1 = Output2 = Output3 = 0
    if class0:
           Output1 = class0 * np.log2(class0)
    if class1:
           Output2 = class1 * np.log2(class1)
    if class2:
           Output3 = class2 * np.log2(class2)
           
    return (-(Output1 + Output2 + Output3 ))