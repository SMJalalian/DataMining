#Sparse Matrix
from Packages.Common import *
from Packages.MatrixHelper import *
#*******************************************************
clearScreen()
MyMatrix = Get_Matrix()
#************ Convert to Sparse form ********************
SparseMatrix = Get_Sparse_Matrix(MyMatrix)
print("############### Spars form ##############")
Print_Matrix(SparseMatrix)
#************ Convert to transpose form ********************
TransposeMatrix = Get_Transpose_Matrix(MyMatrix)
print("############# transpose form #############")
Print_Matrix(TransposeMatrix)
#************ Sum of two matrix ********************
SumMatrix = Add_Simple_Matrix(MyMatrix,MyMatrix)
print("############# Sum of Two Simple Matrix #############")
Print_Matrix(SumMatrix)
print("############# Sum of Two Sparse Matrix #############")
Print_Matrix(SumMatrix)
