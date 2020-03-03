from datetime import datetime
 
start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()




def CreateFunction(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 60*60
    elif span == 'd':
        sec = 60*60*24
    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]'''.format(sec)
    exec(source, globals())
    return f

function_m = CreateFunction('m')
function_h = CreateFunction('h')
function_d = CreateFunction('d')

print(function_m(start,end))
print(function_h(start,end))
print(function_d(start,end))
