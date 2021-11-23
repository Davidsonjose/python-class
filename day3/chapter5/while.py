x = 1
while x <= 6:
    print(x)
    x +=1
states = ['Imo', 'Abia', 'Enugu', 'Anambra', 'Ebonyi'] 
x = 0
while x < 5:
  print(states[x])
  x += 1


# total = 1 + 2 + 3 + 4 ............. 30

x = 1
total = 0
while x <= 30:
    total += x
    x += 1
print(total)


# all = [ '1,', '2,', '3,', '4,', '5,', '9,', '10']
# x = 0
# while x < 7:
#     print(all[x])
#     x += 1


x = 1
while x <= 10:
    if x < 10:
        print(f'{x},')
    else:
        print(x)
    x += 1
x = 1


while x <= 10:
    print(f'{x},')
    x += 1
 

# another way of calculating even numbers
# x = 2
# while x <= 20:
#     print(x)
#     x += 2

x = 1 
while x <= 20:
    if x % 2 == 0:
        if x < 20:
            print(f'{x},')
        else:
            print(x)
    x +=1
