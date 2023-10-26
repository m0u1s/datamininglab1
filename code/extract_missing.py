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
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if(matrix[i][j] == ''):
                missing.append(j)
                continue
    #Print out
    return missing
    """
    transposeMatrix = []
    transpose(matrix, transposeMatrix)
    for _ in missing:
        print(attribute[_] + ":")
        print(transposeMatrix[_])
        print("-----------------------------")
    """
    
