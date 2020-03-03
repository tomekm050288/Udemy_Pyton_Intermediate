import csv
import datetime
import os
import time
#bonanza = {'Batman' : 23.33 , 'Superman': 23.33, 'Wonder Woman' : 23.33, 'Spiderman' : 23.33,'Thor' : 23.33}
path = r"C:\Users\Tomasz\Desktop\udemy cheatsheet\zadania\materiały\products (1).csv"

with open(path,'r') as csvfile:
    bonanza_obj = csv.reader(csvfile, delimiter = ',')
    next(bonanza_obj) # pominięcie nagłówków
    bonanza = {}
    for row in bonanza_obj:
        bonanza[row[0]] = float(row[1])


print(bonanza)
chart = []
total_amount = 0
print("Welcome to T-Shirt Bonanza Shop")
list_of_shirts = list(bonanza.keys())

while True:
    for i in range(len(list_of_shirts)):
        print("{}) {}".format(i+1,list_of_shirts[i]))
    item = input("Please select your option: ")
    if item == '1':
        tshirt = list_of_shirts[int(item)-1]
        chart.append(tshirt)
        print("{} was added to your chart".format(tshirt))
        total_amount += bonanza[tshirt]
        print('if you want to checkout your chart enter "checkout"')
        continue
    elif item == '2':
        tshirt = list_of_shirts[int(item)-1]
        chart.append(tshirt)
        print("{} was added to your chart".format(tshirt))
        total_amount += bonanza[tshirt]
        print('if you want to checkout your chart enter "checkout"')
        continue
    elif item == '3':
        tshirt = list_of_shirts[int(item)-1]
        chart.append(tshirt)
        print("{} was added to your chart".format(tshirt))
        total_amount += bonanza[tshirt]
        print('if you want to checkout your chart enter "checkout"')
        continue
    elif item == '4':
        tshirt = list_of_shirts[int(item)-1]
        chart.append(tshirt)
        print("{} was added to your chart".format(tshirt))
        total_amount += bonanza[tshirt]
        print('if you want to checkout your chart enter "checkout"')
        continue
    elif item == '5':
        tshirt = list_of_shirts[int(item)-1]
        chart.append(tshirt)
        print("{} was added to your chart".format(tshirt))
        total_amount += bonanza[tshirt]
        print('if you want to checkout your chart enter "checkout"')
        continue
    elif item == 'checkout':
        print("Your chart: {}".format(chart))
        print("Total amount: {}".format(round(total_amount,2)))
        break
    else:
        input("Enter valid number!")
        continue

no_duplicates_chart = list(set(chart))

number=1
path2 = r"C:\Users\Tomasz\Desktop\udemy cheatsheet\zadania\materiały\rachunek.txt"
with open(path2, "a") as file:
    file.write("Receipt: {}\n".format(number))
    file.write("Date: {}\n".format(datetime.date.today()))
    file.write("\n")
    file.write("{:12}{:8}{:12}{:6}\n".format("Item", "Qty","Price", "Total"))
    file.write("*"*38)
    file.write("\n")
    for item in no_duplicates_chart:
        file.write("{:15}{:6}{:12}{:5}\n".format(item,str(chart.count(item)),str(bonanza[item]),round((bonanza[item]*chart.count(item)),2)))
    file.write("*"*38)
    file.write("\n")
    file.write("{:32}{:6}\n\n".format(" ",round(total_amount,2)))
print("Receipt printed !!")


print(time.ctime(os.path.getmtime(path2)))



