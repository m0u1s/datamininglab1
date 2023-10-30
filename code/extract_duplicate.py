import readFile
import output

def extract_duplicate(matrix: list):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    duplicate_rows = []
    for i in range(0, num_rows):
        for j in range(i+1, num_rows):
            if matrix[i] == matrix[j]:
                duplicate_rows.append(j)
    
    #check again to delete duplicate value in duplicate_rows
    duplicate_rows = list(set(duplicate_rows))
    return duplicate_rows
def outputMatrix(matrix: list, duplicate_rows: list):
    out = []
    for i in range(0, len(matrix)):
        if i not in duplicate_rows:
            out.append(matrix[i])
    return out
#code run
dup_row= extract_duplicate(readFile.myMatrix)
out_matrix= outputMatrix(readFile.myMatrix, dup_row)

output.outputFile(out_matrix, readFile.at)