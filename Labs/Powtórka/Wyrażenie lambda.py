text_list = ['x','xxx','xxxxx','xxxxxxx','']
napis = 'wyrażenie'
f = lambda x: len(x)

print(f(napis))

for i in text_list:
    print(f(i))


result = list(map(f,text_list))
print(result)

print(list(map(lambda x: len(x),text_list)))