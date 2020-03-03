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


    def __repr__(self):
        return "Kind: {}, name {}, additives {}".format(self.kind,self.name,self.additives)

    def __iadd__(self, other):
        if type(other) is list:
            self.additives.extend(other)
            return self
        elif type(other) is str:
            self.additives.append(other)
            return self
        else:
            raise Exception("Type not implemented {}".format(type(other)))



cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

print(cake01)

cake01 += ['coco','sugar']
cake01.show_info()

cake01 += 'black powder'
cake01.show_info()
