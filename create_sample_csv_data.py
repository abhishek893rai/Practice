import datetime

try:
    with open('sample.csv','a') as csvFile:
        for i in range(11):
            csvFile.write(str(datetime.datetime.today() + datetime.timedelta(days =i)))
            csvFile.write('\n')
        csvFile.close()

except Exception as e:
    print(str(e))