a = b = c = 10
print(id(a), id(b), id(c))
print(a,b,c)
print(type(a) , type(b), type(c))

a = 20
b = c = 10
print(id(a), id(b), id(c))
print(a,b,c)
print(type(a) , type(b), type(c))

a = b = c = [1,2,3]
print(id(a), id(b), id(c))
print(a,b,c)
print(type(a) , type(b), type(c))

a = [1,2,3,4]
b = c = [1,2,3]
print(id(a), id(b), id(c))
print(a,b,c)
print(type(a) , type(b), type(c))

x = 10
y = 10
print(x, y)
print(id(x), id(y))


x = 10
y = y + 1 - 1
print(x, y)
print(id(x), id(y))

x = 10
y = y + 1234567890 - 1234567890
print(x, y)
print(id(x), id(y))










