import readFile
import output

def transpose(l1, l2): 
    for i in range(len(l1[0])):
        row =[]
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

def extract_missing(matrix: list, attribute: list):
    num_rows= len(matrix)
    num_cols= len(matrix[0])
    missing = []
    #track and mark the cols with missing value
    for j in range(0, num_cols):
        for i in range(0, num_rows):
            if(matrix[i][j] == ''):
                missing.append(j)
                break
    #Print out
    return missing

def missing_columns_matrix(matrix: list, missing: list, atr: list):
    missing_matrix = []
    n = len(matrix) 
    fields = []
    for _ in missing:
        fields.append(atr[_])
    for i in range(0, n):
        row = []
        for _ in missing:
            row.append(matrix[i][_])
        missing_matrix.append(row)
    return missing_matrix, fields

#code run
missing= extract_missing(readFile.myMatrix, readFile.at)
matrix, fields= missing_columns_matrix(readFile.myMatrix, missing, readFile.at)

print(len(matrix))
output.outputFile(matrix, fields)  


    