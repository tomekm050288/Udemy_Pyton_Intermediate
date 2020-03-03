def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2


def generate_values(how,*args):
    for arg in args:
        result = how(arg)
        print(result)

items = list(range(1,15))

print("Result for double function:")
generate_values(double,*items)
print("Result for root function:")
generate_values(root,*items)
print("Result for negative function:")
generate_values(negative,*items)
print("Result for div2 function:")
generate_values(div2,*items)

#---------------------------------------

def generate_values(how, x_table):
    value_list = []

    for x in x_table:
        value_list.append(how(x))

    return value_list


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

