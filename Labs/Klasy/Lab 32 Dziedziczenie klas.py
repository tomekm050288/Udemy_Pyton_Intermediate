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
        print('-'*20)
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text



    def show_info(self):
        super().show_info()
        print("Ocassion:        {}".format(self.occasion))
        print("Shape:        {}".format(self.shape))
        if len(self.ornaments) > 0:
            print("Ornaments:")
            for a in self.ornaments:
                print("\t\t{}".format(a))
        print("Text:        {}".format(self.text))


birthday = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',
                       'birthday', 'standard', ['hearts'], '15')
wedding  = SpecialCake('Vanilla Cake','cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                       'wedding', 'pyramid', ['pigeons'], 'Patricia & Tom')


birthday.show_info()
wedding.show_info()

for item in SpecialCake.bakery_offer:
    print(item.full_name)
    item.show_info()










