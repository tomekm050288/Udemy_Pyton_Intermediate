import os
import urllib.request
import sys

data_dir = r'd:\python'

pages = [{ 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
         { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
         { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    try:
        for key, value in page.items():
            if key == 'name':
                path = os.path.join(data_dir,page[key]) + '.html'
                print("Processing: {}  => {} ...".format(page["url"], path))
                urllib.request.urlretrieve(page['url'],path)
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
else:
    print('All pages downloaded successfully!!!')

# i = 0
# while i<len(pages):
#     for key, value in pages[i].items():
#         try:
#             if key == 'name':
#                 path = os.path.join(data_dir, pages[i][key]) + '.html'
#                 urllib.request.urlretrieve(pages[i]['url'],path)
#         except:
#             print("Error",sys.exc_info()[0])
#     i+=1
#     print(path)
# else:
#     print("Pomyślnie wykonano łączenie")