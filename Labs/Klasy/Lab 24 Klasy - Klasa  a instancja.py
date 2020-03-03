class Cake:

        known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
        bakery_offer = []
        
        def __init__(self,name,kind,taste,additives,filling,gluten_free):
                self.name = name
                if kind in Cake.known_types:
                        self.kind = kind
                else:
                        self.kind = 'other'
                self.taste = taste
                self.additives = additives
                self.filling = filling
                self.__gluten_free = gluten_free
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
                print("-" *20)
        
        def set_filling(self,filling):
                self.filling = filling
                
        def add_additives(self,additives):
                for i in additives:
                        self.additives.append(i)
                
                
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['fruits', 'chocolate'],'chocolate mass',True)
cake02 = Cake('Orange Cookies', 'meringue', 'orange', ['carmel', 'frosting'],'fruit mass',True)
cake03 = Cake('Raspberry muffins', 'muffin', 'raspberry', ['topping', 'powdered sugar'],'caramel mass',False)
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',False)



cake04.set_filling('cream filling')
cake04.add_additives(['cocoa powder','coconuts'])

print("Today in our offer:")
for cake in Cake.bakery_offer:
        cake.show_info()
        
cake01.__gluten_free = False
setattr(cake02,'__gluten_free',False)

cake03._Cake__gluten_free = True
cake03.show_info()

##print("Vars cake 02: ", vars(cake02))
##print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
##print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
##print('vars cake01', vars(cake01))
##print('vars Cake', vars(Cake))
##print('dir cake01', dir(cake01))
##print('dir Cake', dir(Cake))

                
