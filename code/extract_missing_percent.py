import readFile
import output

def extract_percent_missing_rows(matrix: list, percent: float): # need argument percent code
    def count_missing_row(row: list):
        count = 0
        for i in row:
            if i == '':
                count += 1
        return count
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    missing_rows = []
    for i in range(0, num_rows):
        if count_missing_row(matrix[i]) > (percent  * len(matrix[i])):
            missing_rows.append(i)
    return missing_rows

def outputMatrix(matrix: list, missing_rows: list):
    out = []
    for i in range(0, len(matrix)):
        if i not in missing_rows:
            out.append(matrix[i])
    return out

#code run
threshold= float(input('Threshold (Default= 0.5): '))
missing = extract_percent_missing_rows(readFile.myMatrix, threshold)

out_matrix= outputMatrix(readFile.myMatrix, missing)

output.outputFile(out_matrix, readFile.at)
 
