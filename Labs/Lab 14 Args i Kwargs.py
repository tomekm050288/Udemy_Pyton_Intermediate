def calculate_paint(efficency_ltr_per_m2,*args):
    for i in args:
        quantity = efficency_ltr_per_m2 * i
        print(quantity)


calculate_paint(3,40,50,60,70,80,90)

rooms_m2 = [100,40,50,70,90]

calculate_paint(3,*rooms_m2)


def log_it(*args):
    filepath = r'd:/python/newtext.txt'
    for i in args:
        with open(filepath,"a") as file:
            file.write(i)
            file.write(" ")
    with open(filepath, "a") as file:
        file.write('\n')
    return


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

#-----------------------------

def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint


print(calculate_paint(0.25, 42, 28, 30))

rooms = [42, 28, 30]
print(calculate_paint(0.25, *rooms))

#-----------------------------

def log_it(*args):
    path = r'd:/python/newtext.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')