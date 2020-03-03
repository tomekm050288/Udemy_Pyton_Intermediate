def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2




def generate_values(funkcja, lista):
    lista_wyników = []
    for i in lista:
        wynik = funkcja(i)
        lista_wyników.append(wynik)
    print(lista_wyników)


#-----------------------------------------------

lst = list(range(1,50,2))
#list_function = [double,root,negative,div2]

def generate_values2(funkcja, lista):
    lista_wyników = []
    for i in lista:
        lista_wyników.append(funkcja(i))
    return lista_wyników

##generate_values2(div2,lst)

x_table = list(range(11))
 
print(generate_values2(double, x_table))
print(generate_values2(root, x_table))
print(generate_values2(negative, x_table))
print(generate_values2(div2, x_table))


 
##def generate_values(how, x_table):
## 
##    value_list = []
##    
##    for x in x_table:
##        value_list.append(how(x))
## 
##    return value_list
## 
## 
##x_table = list(range(11))
## 
##print(generate_values(double, x_table))
##print(generate_values(root, x_table))
##print(generate_values(negative, x_table))
##print(generate_values(div2, x_table))





