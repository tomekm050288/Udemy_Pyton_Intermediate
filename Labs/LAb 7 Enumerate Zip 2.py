projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for k,i,j in zip(projects,leaders,dates):
    print('The leader of {}  started {} is {}'.format(k,j,i))


for a, (k,i,j) in enumerate(zip(projects,leaders,dates)):
    print('{} - The leader of {}  started {} is {}'.format(a,k,j,i))
