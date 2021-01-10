# Remove odd index characters from an string
import os
def clear(): os.system( 'cls' )
clear()
print("Please Enter a Text: " , end =" ")
inputString = input()
Outputstring = ""
length = len(inputString)
i = 0
while i <= length:
    Outputstring += inputString[i]
    i +=2
    pass
print("\n")
print("The new string is equal to: ",Outputstring)
