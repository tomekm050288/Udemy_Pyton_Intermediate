class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

# Druga metoda z dekoratorem

    @property
    def change_text(self):
        return self.__text

    @change_text.setter
    def change_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))


    # pierwsza metoda na property
    #Text = property(__get_text, __set_text, None, 'Text on the cake')



cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

#cake01.Text = 'Happy birthday!'
#cake02.Text = '18'

#for c in Cake.bakery_offer:
    #c.show_info()

cake01.change_text = 'Urodzinowy Tort 2020'
cake02.change_text = '2019'

for c in Cake.bakery_offer:
    c.show_info()

# funkcja eksportująca dane do pliku HTML
import types

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

#static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, 'd:/python/CakeClass/cake01.html')


# funkcja działająca na klasie
def export_1_cake_to_html(cls, path):
    template_header = """
    <table border=1>"""
    template_data = """
         <tr>
           <th colspan=2>{}</th>
         </tr>
         <tr>
             <td>Kind</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Taste</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Additives</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Filling</td>
             <td>{}</td>
           </tr>"""
    template_footer = """</indent>
    </table>"""

    with open(path, "w") as f:
        f.write(template_header)
        for cake in cls.bakery_offer:
            content = template_data.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
            f.write(content)
        f.write(template_footer)

#przypisanie funkcji do klasy - class method
Cake.export_all_cakes_to_html = types.MethodType(export_1_cake_to_html,Cake)
Cake.export_all_cakes_to_html(r'd:/python/CakeClass/exportCake.html')


# funkcja działająca na instacji
def export_1_cake_to_html_inst(self, path):
    template = """
    <table border=1>
         <tr>
           <th colspan=2>{}</th>
         </tr>
           <tr>
             <td>Kind</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Taste</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Additives</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Filling</td>
             <td>{}</td>
           </tr>
    </table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

# instance method
for cake in Cake.bakery_offer:
    cake.export_this_cake_to_html = types.MethodType(export_1_cake_to_html_inst,cake)
    cake.export_this_cake_to_html(r'd:/python/CakeClass/{}.html'.format(cake.name.replace(" ","_")))