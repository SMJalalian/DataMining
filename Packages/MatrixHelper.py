#***************** Read Matrix **********************
def Get_Matrix ():
    Rows = int(input("Please Enter a number for Rows: "))
    Cols = int(input("Please Enter a number for Cols: " ))
    output = [] 
    print("Enter each item value (Enter as a separator) :") 
    for i in range(Rows):
        temp =[] 
        for j in range(Cols):
            temp.append(int(input('( ' + str(i) +' , ' + str(j) + ') : ')))
        if i < Rows -1 :
            print("Next Row ..... ") 
        output.append(temp)
    return output
#***************** Get Dimensions **********************
def Get_Matrix_Row_Numbers(input):
    return len(input)

def Get_Matrix_Col_Numbers(input):
    return len(input[0])
#**************** Check Size Equality ************************
def Is_SimpleMatrix_SameSize(input1, input2):
    if (Get_Matrix_Row_Numbers(input1) == Get_Matrix_Row_Numbers(input2) and Get_Matrix_Col_Numbers(input1) == Get_Matrix_Col_Numbers(input2)) :
        return True
    else :
        return False
#*************************************************
def Get_Sparse_Matrix(input):
    SparseMatrix = []
    rows = Get_Matrix_Row_Numbers(input)
    cols = Get_Matrix_Col_Numbers(input)
    for i in range(rows):
        for j in range(cols):
            if input[i][j] != 0:
                temp = [i,j,input[i][j]]
                SparseMatrix.append(temp)
    return SparseMatrix
#*************************************************
def Get_Transpose_Matrix(input):
    TransposeMatrix = []
    rows = Get_Matrix_Row_Numbers(input)
    cols = Get_Matrix_Col_Numbers(input)
    for i in range(cols):
        temp =[]
        for j in range(rows):
            temp.append(input[j][i])
        TransposeMatrix.append(temp)
    return TransposeMatrix
#*************************************************
def Add_Simple_Matrix(input1 , input2):
    if  Is_SimpleMatrix_SameSize(input1,input2):
        SumMatrix = []
        rows = Get_Matrix_Row_Numbers(input1)
        cols = Get_Matrix_Col_Numbers(input1)
        for i in range(rows):
            temp =[]
            for j in range(cols):
                temp.append(input1[i][j] + input2[i][j])
            SumMatrix.append(temp)
        return SumMatrix
    else :
        return "Error ... Inconsistent dimension."
#*************************************************
def Print_Matrix(input):
    output = ""
    spaceFactor = GetLongestItem(input) + 1
    rows = Get_Matrix_Row_Numbers(input)
    cols = Get_Matrix_Col_Numbers(input)
    for i in range(rows):
        temp = " | "
        for j in range(cols):
            temp += str(input[i][j])
            addSpace = int(spaceFactor - len(str(input[i][j])))
            for space in range(addSpace):
                temp += " "
        temp+="|\n"
        output += temp
    print(output)
#*************************************************
def GetLongestItem(inputMatrix):
    longest = 0
    rows = Get_Matrix_Row_Numbers(inputMatrix)
    cols = Get_Matrix_Col_Numbers(inputMatrix)
    for i in range(rows):
        for j in range(cols):
            number = str(inputMatrix[i][j])
            if len(number) > longest:
                longest = len(number)
    return longest