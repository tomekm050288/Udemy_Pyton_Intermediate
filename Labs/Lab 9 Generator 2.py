ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


routes1 = ((start, stop) for start in ports for stop in ports)

counter1 = 0
for (start, stop) in routes1:
    try:
        print("{} - {}".format(start, stop))
        counter1 += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter1)



routes2 = ((start, stop) for start in ports for stop in ports if start != stop)

counter2 = 0
for (start, stop) in routes2:
    try:
        print("{} - {}".format(start, stop))
        counter2 += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter2)



routes3 = ((start, stop) for start in ports for stop in ports if start < stop)


counter3 = 0
for (start, stop) in routes3:
    try:
        print("{} - {}".format(start, stop))
        counter3 += 1
    except StopIteration:
        print('All values have been generated!')
        break
else:
    print('counter: ', counter3)
