def operation(matrix: list,at: str, row: int, col1: str, col2: str, operation: str, result: str):
    #check the order of col1 and col2 in attribute
    index1, index2 = 0, 0
    for i in range(0, len(at)):
        if(at[i] == col1):
            index1 = i
        if(at[i] == col2):
            index2 = i
    #check if value of col1 in row is numeric
    if not (matrix[row][index1].isnumeric()):
        return "Error: value of col1 in row is not numeric"
    #check if value of col2 in row is numeric
    if not (matrix[row][index2].isnumeric()):
        return "Error: value of col2 in row is not numeric"
    #add result to matrix and attribute
    at.append(result)
    #do operation
    if(operation == '+'):
        matrix[row].append(float(matrix[row][index1]) + float(matrix[row][index2]))
    elif(operation == '-'):
        matrix[row].append(float(matrix[row][index1]) - float(matrix[row][index2]))
    elif(operation == '*'):
        matrix[row].append(float(matrix[row][index1]) * float(matrix[row][index2]))
    elif(operation == '/'):
        matrix[row].append(float(matrix[row][index1]) / float(matrix[row][index2]))
    else:
        return "Error: operation is not valid"
    
    return matrix, at