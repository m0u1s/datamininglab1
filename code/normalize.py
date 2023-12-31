import command_line
import readFile
import output

def attributeIndex(atr: list, cols: list):
    index_arr = []
    for i in cols:
        index_arr.append(atr.index(i))
    return index_arr

def mean(matrix: list, col_index):
    n = len(matrix)
    sum = 0
    for i in range(0, n):
        if(matrix[i][col_index] != ''):
            sum = sum + float(matrix[i][col_index])
    return sum / n

def standard_deviation(matrix: list, col_index):
    n = len(matrix)
    col_mean = mean(matrix, col_index)
    
    sum = 0
    for i in range(0, n):
        if(matrix[i][col_index] != ''):
            sum += (float(matrix[i][col_index]) - col_mean)**2
    sum = sum / (n - 1)

    std = sum ** 0.5
    return std

def find_max(matrix: list, col_index):
    maxi = float(matrix[0][col_index])
    n = len(matrix)

    for i in range(1, n):
        if(matrix[i][col_index] != ''):
            val = float(matrix[i][col_index])
            if(val > maxi):
                maxi = val
    return maxi

def find_min(matrix: list, col_index):
    mini = float(matrix[0][col_index])
    n = len(matrix)

    for i in range(1, n):
        if(matrix[i][col_index] != ''):
            val = float(matrix[i][col_index])
            if(val < mini):
                mini = val
    return mini

def normalize_min_max(matrix: list, col_index):
    n = len(matrix)

    mini = find_max(matrix, col_index)
    maxi = find_min(matrix, col_index)
    diff = maxi - mini
    for i in range(0, n):
        if(matrix[i][col_index] != ''):
            matrix[i][col_index] = (float(matrix[i][col_index]) - mini) / diff

def normalize_z_score(matrix: list, col_index):
    n = len(matrix)

    col_mean = mean(matrix, col_index)
    std_dev = standard_deviation(matrix, col_index)

    for i in range(0, n):
        if(matrix[i][col_index] != ''):
            matrix[i][col_index] = (float(matrix[i][col_index]) - col_mean) / std_dev

def normalize(matrix: list, cols: list, at: list, method = 'min-max'):
    index_cols = attributeIndex(at, cols)

    if method == 'min-max':
        normalize_min_max(matrix, index_cols)
    else: 
        normalize_z_score(matrix, index_cols)

#code run
columns = command_line.columns.split(',')
normalize(readFile.myMatrix, columns, readFile.at, command_line.args.method)

output.outputFile(readFile.myMatrix, readFile.at)