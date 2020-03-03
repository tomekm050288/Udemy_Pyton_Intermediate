import pickle
import glob
import os

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self,name,kind,taste,additives,filling,gluten_free,text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == "":
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(self.name.upper())
        print('Kind: ',self.kind)
        print('Taste: ',self.taste)
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print('Filling: ', self.filling)
        print("Is Gluten free: {}".format(self.__gluten_free))
        print("Napis: ",self.__text)
        print("-" *20)
        
    def set_filling(self,filling):
        self.filling = filling
                
    def add_additives(self,additives):
        for i in additives:
            self.additives.append(i)

    def __get_text(self):
        return self.__text
    
    def __set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))


    def save_to_file(self,path):
        with open(path, 'wb') as f:
            pickle.dump(self,f)

    @classmethod
    def read_from_file(cls,path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(cat_path):
        return glob.glob(cat_path + '/*.bakery')


    Text = property(__get_text,__set_text,None,'Changing of text on cake')

                
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['fruits', 'chocolate'],'chocolate mass',True,'Urodzinowy')
cake02 = Cake('Orange Cookies', 'meringue', 'orange', ['carmel', 'frosting'],'fruit mass',True,'Delicja')
cake03 = Cake('Raspberry muffins', 'muffin', 'raspberry', ['topping', 'powdered sugar'],'caramel mass',False,'Mufinka')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',False,'')

cake04.set_filling('cream filling')
cake04.add_additives(['cocoa powder','coconuts'])

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()
        
cake01.__gluten_free = False
setattr(cake02,'__gluten_free',False)

cake03._Cake__gluten_free = True


cake01.Text = "Urodzinowy Tort 100 lat!!!"
cake01.show_info()

cake03.Text = "WIELKI NAPIS NA MUFFINIE"
cake03.show_info()

cake01.save_to_file(r'd:/python/cake01.bakery')
cake02.save_to_file(r'd:/python/cake02.bakery')
cake05 = Cake.read_from_file(r'd:/python/cake01.bakery')
print("cake05 - stworzone z caka01")
cake05.show_info()

print(Cake.get_bakery_files(r'd:/python'))














##print("Vars cake 02: ", vars(cake02))
##print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
##print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
##print('vars cake01', vars(cake01))
##print('vars Cake', vars(Cake))
##print('dir cake01', dir(cake01))
##print('dir Cake', dir(Cake))
