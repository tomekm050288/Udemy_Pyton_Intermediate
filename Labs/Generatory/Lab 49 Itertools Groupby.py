import os
import itertools
from typing import Dict, List, Any


def scantree(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                yield entry
                yield from scantree(entry.path)
            else:
                yield entry

#
# for i in scantree('d:/python'):
#     print(i)


listing = scantree('d:/python')

# for file in listing:
#     if file.is_dir():
#         print("File:{} is dir".format(file.path))
#     else:
#         print("File:{} is file".format(file.path))

# dir = []
# fil = []
# for file in listing:
#     if file.is_dir():
#         dir.append({'Dir':file.name})
#     else:
#         fil.append({'File':file.name})
#
# print(dir,len(dir))
# print(fil,len(fil))

listing = sorted(listing, key=lambda e: e.is_dir())
for file in listing:
    print(file.name)

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))

