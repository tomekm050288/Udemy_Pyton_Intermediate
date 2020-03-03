import requests
import os
import shutil
import sys



def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'd:/python/tryExcept/'
tmpfile = 'download.tmp'
file = 'spis.html'
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:

    if os.path.isfile(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('Downloading url {}'.format(url))
    save_url_to_file(url,tmpfile_path)
    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)


except requests.exceptions.ConnectionError as e:
    print("Wrong url adres {}".format(url),"/nDetails:/n {}".format(e),"/n",sys.exc_info()[0])

except PermissionError as e:
    print("File opened only to read {}}".format(file_path), "/nDetails:/n {}".format(e), "/n", sys.exc_info()[0])

except FileNotFoundError as e:
    print("File do not exist {}}".format(tmpfile_path), "/nDetails:/n {}".format(e), "/n", sys.exc_info()[0])

except Exception as e:
    print("Error: {}".format(e),sys.exc_info()[0])

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print("End of program")