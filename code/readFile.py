import csv 
from extract_missing import *
from Fill_missing import * 
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def check_properties(matrix: list):
    #return label for each properties e.g: 189, 189 -> numeric ==== mo, 10, ahihi -> categorical 
    #'numeric', 'categorical'
    type = []
    num_rows= len(matrix)
    num_cols= len(matrix[0])
    for i in range(0, num_cols):
        for j in range(0, num_rows):
            if(matrix[j][i] != '' and not ( matrix[j][i].isnumeric() or is_float(matrix[j][i]))):
                type.append('categorical')
                break
        type.append('numeric')
    return type

def readFile(FileName: str):
    matrix = []
    with open(FileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                attribute = row
                line_count += 1
            else:
                matrix.append(row)
                line_count += 1
    csv_file.close()
    return matrix, attribute, line_count

myMatrix, at, l = readFile('D:\DATA_MINING_LAB\Lab1\code\house-prices.csv')
type = check_properties(myMatrix)
print(mean(myMatrix, 3))
fill_mean(myMatrix, 3)
T = []
transpose(myMatrix, T)
print(T[3])