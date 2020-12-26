import math
def Entropy(textObject):
    ent = 0
    for word in textObject.UniqueWords :
        repeat = (list(textObject.AllWords)).count(word)
        temp = (repeat/textObject.AllWordsCount) * (math.log(repeat/textObject.AllWordsCount))
        ent += temp
    return math.fabs(ent)