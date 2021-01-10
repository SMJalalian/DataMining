# Count the number of characters frequency
import os
def clear(): os.system( 'cls' )
clear()
print("Please Enter a Text: " , end =" ")
inputString = (input()).lower()
OutputDic = {} # create an empty dictionary
for item in inputString: # parsing input string, character by character
    if item in OutputDic.keys() : # check if character is alrady exist
        counter = int(OutputDic.get(item)) # find the current value
        counter += 1 # increment the value by 1
        OutputDic.update({item : counter}) # update the value
        pass
    else: # if it was not exist
        OutputDic.update({item : "1" }) # add the character as a new key and set value by 1
        pass
    pass
print("\n")
for key, value in OutputDic.items():
    print( "Character '",key, "' ---> Number of iteration is equal to: ", value)
    pass
print("\n")