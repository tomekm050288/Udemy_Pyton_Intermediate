import datetime as dt

towar1 = {'nazwa' : 'zegarek' }
towar2 = {'nazwa' : 'bransoletka'}
towar3 = {'nazwa' : 'czapka'}

klient1 = {'imię': 'Jack', 'nazwisko':'Strong'}
klient2 = {'imię': 'Dariusz', 'nazwisko':'Jakis'}
klient3 = {'imię': 'Tomasz', 'nazwisko':'Mat'}

transakcja1 = {'data': dt.date(2020,1,30) , 'kupujący' : klient1, 'towar' : towar1}
transakcja2 = {'data': dt.date(2020,1,31) , 'kupujący' : klient2, 'towar' : towar2}
transakcja3 = {'data': dt.date(2020,2,1) , 'kupujący' : klient3, 'towar' : towar3}

towary = [towar1,towar2,towar3]
klienci = [klient1,klient2,klient3]
transakcje = [transakcja1,transakcja2,transakcja3]

def create(list,item):
	if item not in list:
		list.append(item)
	return list

print(create(towary,{'nazwa' : 'komputer'}))


def retrieve(list,item):
	if item in list:
		return item
	else:
		print('Nie ma!')


print(retrieve(towary,{'nazwa' : 'zegarek' }))
	
def update(list,item,klucz,updated_info):
	if item not in list:
		print('Nie ma')
	else:
		index = list.index(item)
		list[index][klucz] = updated_info
		return list

print(update(towary,towar1,'nazwa','Casio'))

def delete(list,item):
	if item in list:
		list.remove(item)
	return list
	
	
towar1={'nazwa' : 'zegarek', 'stanMagazynowy':99}

towar2={'nazwa' : 'bransoletka','stanMagazynowy':1}

def UzupełnijStan(list,towar,ilosc):
	if towar in list:
		index = list.index(towar)
		list[index]['stanMagazynowy'] += ilosc
		return list
	else:
		print('Brak w bazie')
		
		
		
def Sprzedaz(baza,towar,ilosc,klient):
	if towar in baza:
		index = baza.index(towar)
		if ilosc <= baza[index]['stanMagazynowy']:
			baza[index]['stanMagazynowy'] -= ilosc
			nowaTransakcja = {'data':'30.02.2018','kupujacy':klient,'towar': towar,'ilosc': ilosc}
			transakcje.append(nowaTransakcja)
			return baza
		else:
			print('Zbyt niski stan magazynowy')
	else:
		print('towar nie jest w bazie')

	
def zwrot(transakcja,bazaTransakcji,bazaTowarow):
    if transakcja not in bazaTransakcji:
        print('Nie ma takiej transakcji')
    else:
        index=bazaTowarow.index(transakcja['towar'])
        bazaTowarow[index]['stanMagazynowy']+=transakcja['ilosc']
        bazaTransakcji.remove(transakcja)
	
	
	
	
	
	
	
	
	
		
	
	