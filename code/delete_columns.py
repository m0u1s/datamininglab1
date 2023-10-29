import readFile
import output

def countNull(matrix: list, col_index):
    n = len(matrix)
    cnt= 0
    for i in range(0, n):
        if(matrix[i][col_index] == ''):
            cnt+=1
    return cnt

def delColumn(matrix: list):
    del_arr = []
    total_ins= len(matrix)
    n = len(matrix[0])
    for i in range(0, n):
        if countNull(matrix, i) > n / 2:
            del_arr.append(i)
    return del_arr

def outPutMatrix(matrix: list, attribute: list, delete_col: list):
    n = len(matrix) 
    m = len(matrix[0])
    fields = []
    output_matrix = []
    for i in range(0, m):
        if i not in delete_col:
            fields.append(attribute[i])
    for i in range(0, n):
        row = []
        for j in range(0, m):
            if j not in delete_col:
                row.append(matrix[i][j])
        output_matrix.append(row)
    return output_matrix, fields

#code run
delete_columns= delColumn(readFile.myMatrix)
output_matrix, fields =outPutMatrix(readFile.myMatrix, readFile.at, delete_columns)

output.outputFile(output_matrix, fields)  

    