
# مقدار انتروپی هر فایل را محاسبه و چاپ کنید

from Packages.Common import *
from Packages.TextHelper import TextProcessing, Read_All_Files, Generate_WordCloud, Get_RepeatitionOfWords
from Packages.MathHelper import Entropy

clearScreen()

allFiles = Read_All_Files("C:\\Datasets\\")

for key, value in allFiles.items():
    currentText = TextProcessing(key, value.read())
    print("\nThe Entropy of " + key + " is equal to : ", Entropy(currentText))