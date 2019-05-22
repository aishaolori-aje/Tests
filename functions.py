# simply prints the argument passed to it
'''
def writer (arg):
	print(arg)
writer("Hello class")

#converts celcius fahrenheit:
def fahren(T_in_celcius):
	return T_in_celcius * 9/5 + 32
print(fahren(20), "fahrenheit")

fahren_list = []
celcius_list = [20, 5, 10.6, 7, 9]
for x in celcius_list:
	fahren_list.append(fahren(x))
print(fahren_list)
'''

# change a list passed to it:
'''
number1 = int(input("enter numbers"))
number2 = int(input("enter numbers"))
number3 = int(input("enter numbers"))
number4 =int(input("enter numbers"))
number5 = int(input("enter numbers"))

number = number1 + number2 + number3 + number4 + number5
new_number = number/2
print(new_number)


def average():
	list = []
	sum = 0
	x=0
	while len(list) <= 4 :
		item = float(input("enter a number"))
		list.append(item)
		x += 1
	print(list)

	for item in list:
		sum += item
	av = float(sum/len(list))
	print(av)

average()



def far_user ():
	temp_celcius=float(input("Enter a celsius temperature"))
	temp_far = temp_celcius * 9/5 + 32
	print(temp_far, "F")
far_user()
'''
'''  
#keyword parameters
def sum(a, b, c=0, d=0):
	return a-b+c-d
print(sum(12,4))
print(sum(12,4, 5))

#variable scoping by def, variables defined in a function are local to that function
def f():
	print(s)
s = "Python"
f()
def f():
	s = "Clojure"
	print(s)
f()
'''

'''
def f():
    s= "Pearl"
    print(s)

s = "Python"
f()
print(s)

def f():
    s = "Pearl"
    print(s)


s = "Python"
f()
print(s)


def f():
    global s
    print(s)
    s="Dog"
    print(s)
s="Cat"
f()
print(s)
'''
'''
#arbitrary number of parameters
def arithimetic_mean(first, *values):
    return (first + sum(values))/ (1 + len(values))
print(arithimetic_mean(45, 32, 89, 78))
'''
'''
def sum_gp():
   r = float(input("what is the arithimetic ratio?"))
   a = float(input("what is the first term?"))
   n = float(input("What is the size?"))
   return((a*(r**n-1)/r-1))
print(sum_gp())
#pow is defined in python pow(2,3)=8

def average(first, *others):
    return (sum(others))/ (len(others))
print(average(3,2,4))

'''
#Recursive functions
def factorial(n):
    if n ==1:
        return 1

    else:
        s = n*factorial(n-1)
        while True:
            print(f"The {n-1}th factorial is {s}")
            return s

print(factorial(5))
