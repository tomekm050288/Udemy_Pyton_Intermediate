import os
import requests


# generator generujący ścieżki do plików z katalogu ściezka path
def gen_get_files(dir):
    if os.path.isdir(dir):
        for filename in list(os.listdir(dir)):
            Filepath = os.path.join(dir,filename)
            yield Filepath

# for i in gen_get_files(path):
#     print(i)

# Generator - zwraca kolejnie linijki z pliku ścieżka filename
def gen_get_file_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            item = line.replace("\n","")
            yield item


# for file in gen_get_file_lines(r"d:\python\generator\python2.txt"):
#     print(file)

# funkcja pobierająca stronę z adresu url
def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

try:
    os.mkdir(r'd:/python/links_to_check')
except:
    pass

with open(r'd:/python/links_to_check/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('d:/python/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')



for file in gen_get_files('d:/python/links_to_check'):
    for line in gen_get_file_lines(file):
        check_webpage(line)
        print('{} - {} - {}'.format(file,line,check_webpage(line)))