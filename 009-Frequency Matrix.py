# ماتریس فراوانی کلنات در کلیه متن ها

from Packages.Common import *
from Packages.TextHelper import TextProcessing, Read_All_Files
from Packages.MatrixHelper import Print_Matrix,CountItem

clearScreen()

allFiles = Read_All_Files("C:\\Datasets\\")
AllObjects = []
AllWords = []
for key, value in allFiles.items():
    currentFile = TextProcessing(key, value.read())
    AllWords += currentFile.UniqueWords
    AllObjects.append(currentFile)

AllUniqueWords = sorted(set(AllWords))

Output = []
for word in AllUniqueWords:
    temp = []
    for fileObject in AllObjects:
        temp.append(CountItem(fileObject.PurifiedWords , word))
    Output.append(temp)

Print_Matrix(Output)