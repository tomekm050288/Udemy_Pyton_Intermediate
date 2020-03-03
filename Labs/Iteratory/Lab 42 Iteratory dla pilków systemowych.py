import csv

with open('d:/python/iteratory.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #for row in csvreader:
        #print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break
    print('All data was processed')