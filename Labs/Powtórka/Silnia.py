import math

def Power(x):
    silnia = 1
    for i in range(1, x+1):
        silnia = silnia*i
    return silnia

print(Power(10))

print(math.factorial(10))