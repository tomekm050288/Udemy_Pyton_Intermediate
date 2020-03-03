import os
import zipfile
import requests
import datetime as dt

class FileFromWeb:

    def __init__(self,url,tmp_file):
        print("init", dt.datetime.now().isoformat())
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        print('entering')
        response = requests.get(self.url)
        with open(self.tmp_file,'wb') as file:
            print("Zapisywanie zawartości url")
            file.write(response.content)
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit",dt.datetime.now().isoformat())
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip','d:/python/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        print("Zmiana dirctory i wypakowanie pliku")
        os.chdir('d:/python/context')
        z.extract(a_file, '.', None)


