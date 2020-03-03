import random

def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    while True:
        numbers = []
        trial += 1
        for i in range(number_of_values):
            los = random.randint(1,101)
            numbers.append(los)
        if sum(numbers) == asserted_sum:
            yield ((trial,numbers))
            trial = 0


for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)
