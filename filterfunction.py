import random

numbers = []

for i in range(1000000):
    numbers.append(random.randint(1,10000))


def filterNumbers(x):
    if x > 10 :
        return False
    else:
        return True
    

numbers = filter(filterNumbers,numbers)

for i in numbers:
    print(i)