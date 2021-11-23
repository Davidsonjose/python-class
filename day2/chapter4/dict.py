person = {
    'Name': 'Davidson',
    'Age': 10,
    'Status': False,
    'Complexion': 'Chocolate'
}

print(person['Name'])
print(person.get('Name'))
print(person['Age'])
print(person['Status'])
print(person['Complexion'])


person['Status'] = True
if person['Status'] == True:
    print(f"{person['Name']} is married and is age is {person['Age']}")