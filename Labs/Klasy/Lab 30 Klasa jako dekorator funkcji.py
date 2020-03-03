class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

# wykonanie dodatkową klasą i dekoratorem

class NoDuplicates:
    def __init__(self,func):
        self.func = func

    def __call__(self,cake,additives):
        no_duplicate_list = []
        for i in additives:
            if i not in cake.additives:
                no_duplicate_list.append(i)
        self.func(cake, no_duplicate_list)


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


list_of_new_additives = ['strawberries', 'sugar-flowers','chocolade', 'nuts']
add_extra_additives(cake01,list_of_new_additives)

cake01.show_info()

add_extra_additives(cake01,['strawberries', 'sugar-flowers'])

cake01.show_info()


# to samo zrobione funkcją zewnętrzna
def add_extra_additives(cake, additives):
    lst = []
    for i in additives:
        if i not in cake.additives:
            lst.append(i)
    cake.add_additives(lst)

add_extra_additives(cake01,['ooooooooo','strawberries', 'sugar-flowers'])
cake01.show_info()




