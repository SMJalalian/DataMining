# ماتریس فراوانی کلیه متن ها

from Packages.Common import *
from Packages.TextHelper import TextProcessing, Read_All_Files, Generate_WordCloud, Get_RepeatitionOfWords
from Packages.MathHelper import Entropy
from Packages.MatrixHelper import Print_Matrix,CombineAllWordsAsMatrix,GetIterationMatrixWordIndex,GetIterationMatrixFileIndex

clearScreen()

allFiles = Read_All_Files("C:\\Datasets\\")
Output = []
AllObjects = []
allWords = []
for key, value in allFiles.items():
    currentText = TextProcessing(key, value.read())
    AllObjects.append(currentText)

RawIterationMatrix = CombineAllWordsAsMatrix(AllObjects)

for file in AllObjects:
    worlList = file.AllWords
    fileIndex = GetIterationMatrixFileIndex( RawIterationMatrix, file.DoccumentName)
    for word in worlList:
        wordIndex = GetIterationMatrixWordIndex( RawIterationMatrix , str.lower(word))
        newCount = int(RawIterationMatrix[wordIndex][fileIndex]) + 1
        RawIterationMatrix[wordIndex][fileIndex] = newCount
    pass
print(RawIterationMatrix)