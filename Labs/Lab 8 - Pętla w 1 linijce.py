ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# new_ports_lst = []
# for port1 in ports:
#     for port2 in ports:
#         if port1 == port2:
#             continue
#         else:
#             new_ports_lst.append((port1,port2))
# print(new_ports_lst)
# print(len(new_ports_lst))


connections = [(a,b) for a in ports for b in ports if a!=b]
print(connections)
print(len(connections))

for i in connections:
    for j in connections:
        if i == j[-1::-1]:
            connections.remove(j)

print(connections)
print(len(connections))


#---------------------------

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))



