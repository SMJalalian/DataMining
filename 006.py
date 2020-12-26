
# فراوانی تکرار هر کلمه کلیدی را در متن محاسبه و چاپ کنید

from Packages.Common import *
from Packages.TextHelper import TextProcessing, Read_All_Files, Generate_WordCloud, Get_RepeatitionOfWords
from Packages.MathHelper import Entropy

clearScreen()

allFiles = Read_All_Files("C:\\Datasets\\")

for key, value in allFiles.items():
    print("*****  " + key + " File Information  ********\n")
    currentText = TextProcessing(key, value.read())
    print(Get_RepeatitionOfWords(currentText.AllWords , currentText.UniqueWords))
    input("\n Press Enter To Generate Next file Report ....\n\n")