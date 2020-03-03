def name_sorter(names_list):
    male = []
    female = []
    for i in names_list:
        if i[-1] == 'a':
           female.append(i)
        else:
            male.append(i)
    dict = {'female' : female, 'male' : male}
    return dict


print(name_sorter(['Tomasz','Katarzyna','Barbara','Grzegorz','Andrzej','Ada']))
