projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for i in range(0,len(projects)):
    print("The leader of {} is {}".format(projects[i],leaders[i]))

new_lst = list(zip(projects,leaders))
print(new_lst)
for i in range(0,len(projects)):
    print("The leader of {} is {}".format(new_lst[i][0], new_lst[i][1]))

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p, l))