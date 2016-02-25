import csv

try:
    with open('sample.csv') as csvFile:    # no need to close file when using 'with-as' statement
        csvData = csv.reader(csvFile,delimiter=' ')  # delimiter is a space
        for row in csvData:
            print(row)
except Exception as e :
    print(str(e))
