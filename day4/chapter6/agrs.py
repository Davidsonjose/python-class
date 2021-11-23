# VARIABLE LENGTH KEYWORD ARGUEMENT

# def addition(var1, var2):
#     print(var1 + var2)


# addition(10, 5)


def addition(*args):
    total = 0
    for a in args:
        total += a
    print(total)


addition(10, 5, 3)



def multiplication(*args):
    total = 1
    for a in args:
        total *=a 
    print(total)

multiplication(3, 2, 2):



def show_state(*args):
    for s in args:
        print(s)

show_state('Imo', 'Abia')

show_state('Imo', 'Abia', 'Akwa-ibom', 'Abuja')