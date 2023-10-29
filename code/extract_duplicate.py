def extract_duplicate(matrix: list):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    duplicate_rows = []
    for i in range(0, num_rows):
        for j in range(i+1, num_rows):
            if matrix[i] == matrix[j]:
                duplicate_rows.append(j)
    
    #check again to delete duplicate value in duplicate_rows
    for i in range(0, len(duplicate_rows)):
        for j in range(i+1, len(duplicate_rows)):
            if duplicate_rows[i] == duplicate_rows[j]:
                duplicate_rows.pop(j)
    return duplicate_rows #return list of duplicate rows