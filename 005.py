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
    MyMatrix.append(temp)
#************ Convert to Sparse form ********************
SparseMatrix = []
R=0
for Row in MyMatrix:
    C=0
    for item in Row:
        if item != 0:
            temp = [R,C,item]
            SparseMatrix.append(temp)
        C+=1
    R+=1
print("############### Spars form ##############")
print(SparseMatrix)
#************ Convert to transpose form ********************
TransposeMatrix = []
for i in range(Cols):
    temp =[]
    for j in range(Rows):
        temp.append(MyMatrix[j][i])
    TransposeMatrix.append(temp)
print("############# transpose form #############")
print(TransposeMatrix)
#************ Sum of two matrix ********************
SumMatrix = []
for Row in MyMatrix:
    temp =[]
    for item in Row:
        temp.append(item + item)
    SumMatrix.append(temp)
print("############# Sum of Two Matrix #############")
print(SumMatrix)
