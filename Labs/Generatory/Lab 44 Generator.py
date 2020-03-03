def Combinations(products,promotions,customers):
    for i in range(len(products)):
        for j in range(len(promotions)):
            for k in range(len(customers)):
                item_to_return = "{} - {} -{}".format(products[i],promotions[j],customers[k])
                yield item_to_return




products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]


for d in Combinations(products,promotions,customers):
    print(d)


def combinations(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield ("{} - {} - {}".format(i, j, k))


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

print("--------------------------------------")
for c in combinations(products, promotions, customers):
    print(c)