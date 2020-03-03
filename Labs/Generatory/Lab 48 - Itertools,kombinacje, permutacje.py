import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
lst = []

for comb in it.permutations(notes,4):
    lst.append(comb)
    print(comb)


print(len(lst))

# wariancja bez powtórzeń - czyli permuatacja - wzor na ilość komb

V = math.factorial(len(notes)) / math.factorial(len(notes) - 4)
print(int(V))

lst2 = []
for comb in it.combinations_with_replacement(notes,4):
    lst2.append(comb)
    print(comb)

print(len(lst2))

# Wariancja z powtórzeniami wzór

VP = math.pow(len(notes),4)
print(int(VP))

input('Press enter')
lst3 = []
for x in it.product(notes,repeat=4):
    lst3.append(x)
    print(x)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
    pow(len(notes), 4)))

print(len(lst3))











