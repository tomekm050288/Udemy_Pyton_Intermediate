import time

def fib(n):
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

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
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

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
    
