import readFile
import output
import command_line

def operation(matrix: list,at: str, col1: str, col2: str, operation: str, result: str):
    #check the order of col1 and col2 in attribute
    index1, index2 = at.index(col1), at.index(col2)

    #check if value of col1 in row is numeric
    if readFile.type[index1] != 'numeric':
        return "Error: value of col1 row is not numeric"
    #check if value of col2 in row is numeric
    if readFile.type[index2] != 'numeric':
        return "Error: value of col2 is not numeric"
    #add result to matrix and attribute
    at.append(result)
    #do operation

    num_rows= len(matrix)

    for i in range(0, num_rows):
        if matrix[i][index1] == '' or matrix[i][index1] == '':
            return "Error: can not do the operation due to the NULL"
        if(operation == '+'):
            matrix[i].append(float(matrix[i][index1]) + float(matrix[i][index2]))
        elif(operation == '-'):
            matrix[i].append(float(matrix[i][index1]) - float(matrix[i][index2]))
        elif(operation == '*'):
            matrix[i].append(float(matrix[i][index1]) * float(matrix[i][index2]))
        elif(operation == '/'):
            matrix[i].append(float(matrix[i][index1]) / float(matrix[i][index2]))
        else:
            return "Error: operation is not valid"
    
    return matrix, at

op = input('Operation(+, -, *, /): ')
result = command_line.args.col1 + ' ' + op + ' ' +command_line.args.col2
try:
    out_matrix, fields = operation(readFile.myMatrix, readFile.at, command_line.args.col1, command_line.args.col2, op, result)
    output.outputFile(out_matrix, fields)   
except:
    print(operation(readFile.myMatrix, readFile.at, command_line.args.col1, command_line.args.col2, op, result))