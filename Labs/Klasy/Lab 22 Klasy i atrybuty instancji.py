class Cake:
        def __init__(self,name,kind,taste,addictions,filling):
                self.name = name
                self.kind = kind
                self.taste = taste
                self.addictions = addictions
                self.filling = filling
		
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['fruits', 'chocolate'],'chocolate mass')
cake02 = Cake('Orange Cookies', 'cookies', 'orange', ['carmel', 'frosting'],'fruit mass')
cake03 = Cake('Raspberry muffins', 'muffins', 'raspberry', ['topping', 'powdered sugar'],'caramel mass')
cake04 = Cake('Super Sweet Maringue ', 'meringue', 'very sweet', [] ,'nothing')

bakery_offer = [cake01,cake02,cake03]

print("Today in our offer:")
for cake in bakery_offer:
	print('{} - ({}) main taste: {} with additives of {}, filled with {}.'\
              .format(cake.name,cake.kind,cake.taste,cake.addictions,cake.filling))
		
