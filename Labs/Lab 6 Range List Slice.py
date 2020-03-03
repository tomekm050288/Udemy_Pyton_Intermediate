##colors = ["red", "orange", "green", "violet", "blue", "yellow"]
##
##def ColorList(lst,n):
##    return lst[:n]
##
##
##for i in range(1,len(colors)+1):
##    print(ColorList(colors,i))
    

text = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura)
    – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym
    światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych.
    W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do
    wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'''

lst_text = text.split("(")[1]
lst_text2 = lst_text.split(")")[0]
print(lst_text2)


print(text[text.index('(')+1:text.index(')')])


        

