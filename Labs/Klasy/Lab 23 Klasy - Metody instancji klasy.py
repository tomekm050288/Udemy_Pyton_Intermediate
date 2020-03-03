class Cake:
	def __init__(self,name,kind,taste,additives,filling):
		self.name = name
		self.kind = kind
		self.taste = taste
		self.additives = additives
		self.filling = filling

	def show_info(self):
		print('Today in our offer:')
		print(self.name.upper())
		print('Kind: ',self.kind)
		print('Taste: ',self.taste)
		print('Additives: ')
		for i in self.additives:
			print(' '*10,i)
		print('Filling: ', self.filling)	
		print("-" *30)
	
	def set_filling(self,filling):
		self.filling = filling
		
	def add_additives(self,additives):
		for i in additives:
			self.additives.append(i)
		
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['fruits', 'chocolate'],'chocolate mass')
cake02 = Cake('Orange Cookies', 'cookies', 'orange', ['carmel', 'frosting'],'fruit mass')
cake03 = Cake('Raspberry muffins', 'muffins', 'raspberry', ['topping', 'powdered sugar'],'caramel mass')
cake04 = Cake('Super Sweet Maringue ', 'meringue', 'very sweet', [] ,'nothing')


cake04.set_filling('cream filling')
cake04.add_additives(['cocoa powder','coconuts'])
cake04.show_info()

bakery_offer = [cake01,cake02,cake03,cake04]

print("Today in our offer:")
for cake in bakery_offer:
	cake.show_info()
		
