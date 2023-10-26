def count_missing(matrix: list, attribute: list):
    num_rows= len(matrix)
    num_cols= len(matrix[0])
    missing = []
    #track and mark the rows with missing value
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if(matrix[i][j] == ''):
                missing.append(i)
                continue
    #Print out
    """
    for i in missing:
        print(matrix[i])
        print("------------------------")
    """
    return missing