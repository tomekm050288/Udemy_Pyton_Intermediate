import math

argument_list= []
counter = 0

for i in range(0,100):
    argument_list.append(round(counter,2))
    counter+=0.1

print(argument_list)

formula = input("Wrowadz wzór: ")

lista_wyników = []
for x in argument_list:
    wynik = eval(formula)
    lista_wyników.append(wynik)

print(lista_wyników)
    
    

