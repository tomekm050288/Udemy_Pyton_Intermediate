import os
import functools
from datetime import datetime as dt

def wrapper_with_log_file(logged_action, log_file_path):
	def wrapper_with_log_to_known_file(func):
		def the_real_wrapper(path):
			file = open(log_file_path,'a')
			file.write("Action ")
			file.write(logged_action)
			file.write(" executed on ")
			file.write(path)
			file.write(" on ")
			file.write(dt.now().strftime("%Y-%m-%d %H:%M:%S\n"))
			result = func(path)
			file.close()
			return result
		return the_real_wrapper
	return wrapper_with_log_to_known_file
	
@wrapper_with_log_file('FILE_CREATE', r'd:/python/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
	
@wrapper_with_log_file('FILE_DELETE', r'd:/python/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
	
create_file(r'd:\python\dummy_file.txt')
delete_file(r'd:\python\dummy_file.txt')
create_file(r'd:\python\dummy_file.txt')
delete_file(r'd:\python\dummy_file.txt')


#----------------------------------------------------------------
# wrapper z odpowiedzi

import os
from datetime import datetime as dt
import functools


def wrapper_with_log_file(logged_action, log_file_path):

def wrapper_with_log_to_known_file(func):
    
    def the_real_wrapper(path):
       
        with(open(log_file_path,'a')) as f:
            f.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
             
        return func(path)
    
    return the_real_wrapper

return wrapper_with_log_to_known_file

@wrapper_with_log_file('FILE_CREATE',r'c:/temp/file_create.txt')
def create_file(path):
print('creating file {}'.format(path))
open(path,"w+")

@wrapper_with_log_file('FILE_DELETE',r'c:/temp/file_delete.txt')
def delete_file(path):
print('deleting file {}'.format(path))
os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
