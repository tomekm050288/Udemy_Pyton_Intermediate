ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


routes = ((start, stop) for start in ports for stop in ports)

counter = 1
for x in routes:
    try:
        print(next(routes),counter)
        counter += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter)



routes = ((start, stop) for start in ports for stop in ports if start != stop)

counter = 1
for x in routes:
    try:
        print(next(routes),counter)
        counter += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter)



routes = ((start, stop) for start in ports for stop in ports if start < stop)


counter = 1
for x in routes:
    try:
        print(next(routes),counter)
        counter += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter)
