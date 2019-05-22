#PRINT YOUR NAME 100 TIMES
name = 'Olori-Aje Aisha'
lessThan100 = 0
count = 0
while lessThan100 < 100:
    lessThan100 += 1
    while count < 100:
        count += 1
        print(f'{count}. {name}')


number = 0
while number < 20:
    number += 1
    print(f'{number}----{number**2}')


number = (13, 2, 2, 13)
for count in number:
    if count == 13:
        print(f'*' * count)
    else:
        print(f"*" + f"           " + f"*")

num = (1, 2, 3, 4, 5,  6)
for x in num:
    print(f"*" * x)

range = (1, 2, 3, 4)
for line in range:
    if line == 1:
        print ("   *  ")
    if line == 2:
        print(" *  " + "  *")
    if line ==  3:
        print("*"+ " * " + " * " + "*")
    if line == 4:
        print(f"*" + f"      " + f"*")


def factorial(n):
    if n == 1:
        return 1
    else:
       s = n * factorial(n-1)
    return s
print(factorial(4))
import math
print(pow(3, factorial(4)))


def factorial(n):
    if n ==1:
        return 1

    else:
        s = n*factorial(n-1)
        while True:
            print(f"The {n-1}th factorial is {s}")
            return s

print(factorial(5))
