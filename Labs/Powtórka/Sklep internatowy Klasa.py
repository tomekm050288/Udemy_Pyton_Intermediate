import csv
import datetime
import os
import time


class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def GetPrice(self):
        return self.price

    def GetName(self):
        return self.name


class Chart:

    total_price = 0

    def __init__(self):
        self.dict = {}

    def add(self,item):
        if item.name not in self.dict.keys():
            self.dict[item.name] = item.quantity
        else:
            self.dict[item.name] += item.quantity
        Chart.total_price += item.price * item.quantity

    def remove(self,item):
        if Chart.total_price == 0:
            raise Exception("Empty Chart")
        elif self.dict[item.name] > 1:
            self.dict[item.name] -= item.quantity
        else:
            del self.dict[item.name]
        Chart.total_price -= item.price*item.quantity

    def get_total(self):
        return self.dict

path = r"C:\Users\Tomasz\Desktop\udemy cheatsheet\zadania\materiały\products (1).csv"

with open(path,'r') as csvfile:
    bonanza_obj = csv.reader(csvfile, delimiter = ',')
    next(bonanza_obj) # pominięcie nagłówków
    bonanza = {}
    for row in bonanza_obj:
        bonanza[row[0]] = float(row[1])


print("Welcome to T-Shirt Bonanza Shop\n")
print(bonanza, "\n")

list_of_shirts = list(bonanza.keys())
chart = Chart()

while True:
    for i in range(len(list_of_shirts)):
        print("{}) {}".format(i+1,list_of_shirts[i]))
    item = input("Please select your option: ")
    if item == '1':
        quantity = input("How many ?: ")
        tshirt1 = Product(list_of_shirts[int(item)-1],bonanza[list_of_shirts[int(item)-1]],int(quantity))
        chart.add(tshirt1)
        print("{} was added to your chart\n".format(tshirt1.name))
        print('if you want to checkout your chart enter "checkout"\n')
        print('if you want to remove item enter "remove"\n')
        continue
    elif item == '2':
        quantity = input("How many ?: ")
        tshirt2 = Product(list_of_shirts[int(item)-1], bonanza[list_of_shirts[int(item)-1]], int(quantity))
        chart.add(tshirt2)
        print("{} was added to your chart\n".format(tshirt2.name))
        print('if you want to checkout your chart enter "checkout"\n')
        print('if you want to remove item enter "remove"\n')
        continue
    elif item == '3':
        quantity = input("How many ?: ")
        tshirt3 = Product(list_of_shirts[int(item) - 1], bonanza[list_of_shirts[int(item) - 1]], int(quantity))
        chart.add(tshirt3)
        print("{} was added to your chart\n".format(tshirt3.name))
        print('if you want to checkout your chart enter "checkout"\n')
        print('if you want to remove item enter "remove"\n')
        continue
    elif item == '4':
        quantity = input("How many ?: ")
        tshirt4 = Product(list_of_shirts[int(item) - 1], bonanza[list_of_shirts[int(item) - 1]], int(quantity))
        chart.add(tshirt4)
        print("{} was added to your chart\n".format(tshirt4.name))
        print('if you want to checkout your chart enter "checkout"\n')
        print('if you want to remove item enter "remove"\n')
        continue
    elif item == '5':
        quantity = input("How many ?: ")
        tshirt5 = Product(list_of_shirts[int(item) - 1], bonanza[list_of_shirts[int(item) - 1]], int(quantity))
        chart.add(tshirt5)
        print("{} was added to your chart\n".format(tshirt5.name))
        print('if you want to checkout your chart enter "checkout"\n')
        print('if you want to remove item enter "remove"\n')
        continue
    elif item == 'remove':
        print('Your chart: ', chart.get_total(),'\n')
        poz = input("Select product: ")
        qua = input("How many? ")
        tshirt_to_remove = Product(poz,bonanza[poz],int(qua))
        chart.remove(tshirt_to_remove)
    elif item == 'checkout':
        print('Your chart: ', chart.get_total(),'\n')
        print("Total amount: {}".format(round(Chart.total_price,2)))
        break
    else:
        input("Enter valid number!\n")
        continue







