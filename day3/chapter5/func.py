def say_hello():
    print('Hello world!')

# involking the function
say_hello()


def greetings(name):
    print(f'Hello Mr. {name}!')


greetings('Benedict')
greetings('Davidson')
greetings('Peter')





#  write a python function that will print out the code below
# Obasanjo was the president of nigeria in the year 1999 and handed over to yaradua in 2007
# Where obasanjo, Nigeria, 1999, Yaradua, are parameters of the function

# create a python function that will print out the area of a triangle
# given the formular area = 1/2 base * height, where base = 150 and height = 100

# create a python function that will print out the perimeter of a rectangle
# given the formular perimeter = 2(L + B), where L = 200 and B =100


def content(nameOne, country, yearOne, nameTwo, yearTwo):
    print(f'{nameOne} was the president of {country} in the year {yearOne} and handed over to {nameTwo} in {yearTwo}')

content('Obasanjo', 'Nigeria', '1999', 'Yaradua', '2007')


def cal(base, height):
    area = 0.5 * base * height 
    print(int(area))
cal(150, 100)


def cal2(length, breath):
    perimeter = 2 * length + breath
    print (int(perimeter))

cal2(200, 100)

def addition(num1, num2):
    add = num1 + num2
    print(add)


def get_even_numbers(number):
    x = 1 
while x <= (number):
    if x % 2 == 0:
        if x < (number):
            print(f'{x},')
        else:
            print(x)
    x +=1
get_even_numbers(20)

