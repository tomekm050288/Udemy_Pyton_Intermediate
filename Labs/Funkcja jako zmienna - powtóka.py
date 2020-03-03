def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2


number = 20

list = [double,root,negative,div2]

for i in list:
    wynik = i(number)
    print(wynik)
