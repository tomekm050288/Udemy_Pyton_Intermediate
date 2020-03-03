import itertools

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print(get_factors(20))

candidate_list = []
for i in range(1,1001):
    candidate_list.append(i)

excellent_numbers = []
for number in candidate_list:
    if sum(get_factors(number)) == number:
        excellent_numbers.append(number)
print(excellent_numbers)

# znaleznienie wszystkich liczb doskonałych od zakresie 1,1000
filtered_list = itertools.filterfalse(lambda x:sum(get_factors(x)) != x, candidate_list)

for i in list(filtered_list):
    print("Liczba {} posiada dzielniki {} i jest doskonała".format(i,get_factors(i)))



