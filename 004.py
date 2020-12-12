# Get comma separated word and print unique words as sorted form
import os
def clear(): os.system( 'cls' )
clear()
print("Please Enter a csv string in single line: " , end =" ")
inputString = (input()).lower().split(",")
OutputList = [] # create an empty List
for item in inputString: # parsing input List
    if inputString.count(item) == 1 : # check if word is unique
        OutputList.append(item) 
        pass
    pass
OutputList.sort() # sort the output list
print("\n")
print(*OutputList, sep = "\n") 
print("\n")