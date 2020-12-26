
# نمودار وورد کلود را برای هر فایل محاسبه و چاپ کنید

from Packages.Common import *
from Packages.TextHelper import TextProcessing, Read_All_Files, Generate_WordCloud, Get_RepeatitionOfWords
from Packages.MathHelper import Entropy

clearScreen()

allFiles = Read_All_Files("C:\\Datasets\\")

for key, value in allFiles.items():
    currentText = TextProcessing(key, value.read())
    Generate_WordCloud(currentText)