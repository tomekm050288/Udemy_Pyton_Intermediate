import os

filepath = input("Enter newfilepath: ")

text = 'Za oknem jest ciemno zimno i szaro!!'

with open(filepath, "w") as file:
    file.write(text)

def NewFunction(path):
    file = open(path,"r")
    fragment = file.read()
    lista = fragment.split(" ")
    file.close()
    return len(lista)



path = filepath

# if os.path.isfile(path):
#     print("File exists %s " % path)
#     print(NewFunction(path))
# else:
#     print("File dont\'t exist")


os.path.isfile(path) and print("There are {} words in the file {}".format(NewFunction(path),path))


