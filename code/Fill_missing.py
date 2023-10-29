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
 
def median(matrix: list, col_index):
    n = len(matrix)
    k = int(n / 2)

    if(n % 2 == 1):
        if(matrix[k][col_index] != ''):
            return None
        return matrix[k][col_index]
    else:
        if(matrix[k - 1][col_index] != '' or matrix[k][col_index] != ''):
            return None
        return (float(matrix[k - 1][col_index]) + float(matrix[k][col_index])) / 2
    
def mode(matrix: list, col_index):
    freq = {}
    n = len(matrix)
    for i in range(0, n):
        if(matrix[i][col_index] not in freq.keys()):
            freq[matrix[i][col_index]] = 1
        else:
            freq[matrix[i][col_index]] = freq[matrix[i][col_index]] + 1
    sortedFreq = sorted(freq)
    if(sortedFreq[0] == '' and len(sortedFreq) < 2):
        return sortedFreq[1]
    else:
        return sortedFreq[0]

def fill_mean(matrix: list, col_index: int):
    n = len(matrix)
    value = mean(matrix, col_index)
    for i in range(0, n):
        if(matrix[i][col_index] == ''):
            matrix[i][col_index] = str(value)

def fill_median(matrix: list, col_index: int):
    n = len(matrix)
    value = median(matrix, col_index)
    for i in range(0, n):
        if(matrix[i][col_index] == ''):
            matrix[i][col_index] = str(value)

def fill_mode(matrix: list,  col_index: int):
    n = len(matrix)
    value = mode(matrix, col_index)
    for i in range(0, n):
        if(matrix[i][col_index] == ''):
            matrix[i][col_index] = str(value)

def fill_miss_col(matrix: list, cols: list, at: list, method= 'mean'):
    index_cols = attributeIndex(at, cols)

    if(method == 'mean'):
        for i in index_cols:
            fill_mean(matrix, i)
    if(method == 'median'):
        for i in index_cols:
            fill_median(matrix, i)
    if(method == 'mode'):
        for i in index_cols:
            fill_mode(matrix, i)

#code run
columns = command_line.columns.split(',')
fill_miss_col(readFile.myMatrix, columns, readFile.at, command_line.args.method)

output.outputFile(readFile.myMatrix, readFile.at)