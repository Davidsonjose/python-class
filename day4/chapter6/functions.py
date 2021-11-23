def office(name, color= 'Yellow'):
    print(f'The color of Mr {name} is {color}')

office('Benedita')


def get_even_numbers(number, start=1):
    while start <= number:
        if start % 2 == 0:
            if start < number:
                print(f'{start},')
            else:
                print(start)
        start += 1


print('EVEN_NUMBERS 1 ----- 10')
get_even_numbers(10)
print('EVEN NUMBERS 10 ----- 40')
get_even_numbers(40, 10)