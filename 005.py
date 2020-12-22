#Sparse Matrix
import os
def clear(): os.system( 'cls' )
clear()
Rows = int(input("Please Enter a number for Rows: "))
Cols = int(input("Please Enter a number for Cols: " ))
MyMatrix = [] 
print("Enter the entries each row items (Enter as a separator) :") 
for i in range(Rows):
    temp =[] 
    for j in range(Cols):
        temp.append(int(input()))
    if i < Rows -1 :
        print("Next Row ..... ")
        pass    
    MyMatrix.append(temp)
pass
#************ Convert to Sparse form ********************
SparseMatrix = []
R=0
for Row in MyMatrix:
    C=0
    for item in Row:
        if item != 0:
            temp = [R,C,item]
            SparseMatrix.append(temp)
            pass
        C+=1
        pass
    R+=1
    pass
print("############### Spars form ##############")
print(SparseMatrix)
#************ Convert to transpose form ********************
TransposeMatrix = []
for i in range(Cols):
    temp =[]
    for j in range(Rows):
        temp.append(MyMatrix[j][i])
        pass
    TransposeMatrix.append(temp)
pass
print("############# transpose form #############")
print(TransposeMatrix)
#************ Sum of two matrix ********************
SumMatrix = []
for Row in MyMatrix:
    temp =[]
    for item in Row:
        temp.append(item + item)
        pass
    SumMatrix.append(temp)
pass
print("############# Sum of Two Matrix #############")
print(SumMatrix)
#************ Multiply of two matrix ********************
SumMatrix = []
for Row in MyMatrix:
    temp =[]
    for item in Row:
        temp.append(item * item)
        pass
    SumMatrix.append(temp)
pass
print("############# Multiply of Two Matrix #############")
print(SumMatrix)