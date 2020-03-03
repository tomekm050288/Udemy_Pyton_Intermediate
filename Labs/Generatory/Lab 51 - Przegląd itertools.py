# Liczby pierwsze do 1000

import itertools as it

def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


# not optimal:
# prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
# print(prime_numbers[:10])

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))