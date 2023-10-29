import command_line
import readFile
import output

def count_missing(matrix: list):
    num_rows= len(matrix)
    num_cols= len(matrix[0])
    missing = 0
    #track and mark the rows with missing value
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if(matrix[i][j] == ''):
                missing+= 1
                break
    #Print out
    """
    for i in missing:
        print(matrix[i])
        print("------------------------")
    """
    return missing
print(count_missing(readFile.myMatrix))