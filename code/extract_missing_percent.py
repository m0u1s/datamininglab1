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
        if count_missing_row(matrix[i]) >= (percent  * len(matrix[i])):
            missing_rows.append(i)
    return missing_rows