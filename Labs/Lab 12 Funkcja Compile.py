import math
import time

formulas_list = ["abs(x**3 - x**0.5)","abs(math.sin(x) * x**2)"]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)


start = time.time()
print("Start time: ", start)

for formula in formulas_list:
    result_list = []
    print(formula)
    for x in argument_list:
        result_list.append(eval(formula))
    print("Min value: ", min(result_list),"Max value: ", max(result_list))

stop = time.time()
print("Stop time: " , stop)
time_of_calc1 = stop - start
print("Time of calculation: ", time_of_calc1)





start = time.time()
print("Start time: ", start)

for formula in formulas_list:
    compiled_formula = compile(formula,"Internal value", 'eval')
    result_list = []
    print(formula)
    for x in argument_list:
        result_list.append(eval(compiled_formula))
    print("Min value: ", min(result_list),"Max value: ", max(result_list))

stop = time.time()
print("Stop time: " , stop)
time_of_calc2 = stop - start
print("Time of calculation: ", time_of_calc2)

print("Compile %d x faster" % (time_of_calc1/time_of_calc2))







