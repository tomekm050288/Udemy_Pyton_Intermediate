import time

def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time.time()
print('Start time: ', start)
for i in range(1,30):
    print(i)
    print(fib(i))
    part_time = time.time()
    different = part_time - start
    print('Part time: ',different)
end_time = time.time()
print('Final EndTime - StartTime: ', end_time-start)

import functools

@functools.lru_cache(100)
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time.time()
print('Start time: ', start)
for i in range(1,33):
    print(i)
    print(fib(i))
    part_time = time.time()
    different = part_time - start
    print('Part time: ',different)
end_time = time.time()
print('Final EndTime - StartTime: ', end_time-start)
    
print(fib.cache_info())
    
