import csv
import command_line
def outputFile(matrix: list, fields: list):  
    with open(command_line.output, 'w') as f:
    # using csv.writer method from CSV package
        out = csv.writer(f)
        out.writerow(fields)
        out.writerows(matrix)