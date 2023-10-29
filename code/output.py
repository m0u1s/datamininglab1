import csv
import command_line
def outputFile(matrix: list, fields: list):  
    with open(command_line.args.output, 'w', newline='') as f:
    # using csv.writer method from CSV package
        out = csv.writer(f)
        out.writerow(fields)
        for row in matrix:
            out.writerow(row)
    print('done')