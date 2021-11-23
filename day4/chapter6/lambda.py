add = lambda x, y: x+y
print(add(5, 3))


# to do use lambda to multipl 3 numbers 

multiplication = lambda x, y, z: x*y*z
print(multiplication(5, 3, 4))

area = lambda area, height: 0.5 * area * height
print(area(5, 4))

even = lambda x : x if x % 2 == 0 else False
print(even(10))

get_even = list(filter(lambda x : x if x % 2 == 0 else False, range(11)))
print(get_even)


double_even = list(map( lambda x : x * 2, range(1, 11)))
print(double_even)


