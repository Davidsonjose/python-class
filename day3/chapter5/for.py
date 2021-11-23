states = ['imo', 'owerri', 'jigawa']

for s in states:
    print(s)


x = 0
total = 0
for x in range (31):
    total += x
print(total)
x +=1


states = {
    'Imo': 'Owerri',
    'Abi': 'Umahia',
    'Adamawa': 'Yola',
    'Akwa-Ibom': 'Uyo',
    'Lagos': 'Ikeja'
}

# printing all the values 
for state in states:
    print(states[state])


#  printing the state and the values 
for state, capital in states.items():
    print(state + ', ' +capital)

#  for printing the values also 
for capital in states.values():
    print(capital)


states= {
    'South East': {'Imo': 'Owerri', 'Abia': 'Umahia', 'Eboyi': 'Abakaliki', 'Enugu': 'Enugu'},
    'South West': {'Lagos': 'Ikeja', 'Oyo': 'Ibadab', 'Ogun': 'Abeokuta', 'Ondo': 'Akure'},
    'South South': {'Akwa-Ibom': 'Uyo', 'Delta': 'Asaba', 'Rivers': 'Port hacourt', 'Bayelsa': 'Yenuga'}
}



# for state in states:
#     print(state)
#     for state in states.items():
#         print(state)



for zones in states:
    print(zones)
    for state, capital in states[zones].items():
        print(f'{state} => {capital}')

