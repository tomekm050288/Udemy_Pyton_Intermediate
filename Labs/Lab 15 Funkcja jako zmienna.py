def double(x):
    return 2 * x

def root(x):
    return x ** 2

def negative(x):
    return -x

def div2(x):
    return x / 2

number = 8

transformations = [double,root,negative,div2]
tmp_return_value = number

for item in transformations:
    result = item(tmp_return_value)
    print(result)

transformations2 = [root,root,div2,double]

for item in transformations2:
    print(item(tmp_return_value))


def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, root, div2, negative]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

number = 125
transformations = [root, root, div2, double]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))