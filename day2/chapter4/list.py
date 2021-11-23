# python list looks like array in javascript

students = ['Joan', 'Sylvia', 'Diamond', 'Davidson']
print(students[0])


data = ['Obasanjo', 'Nigeria', 1999, 'Yaradua', 2007]
print(f'{data[0]} was the president of {data[1]} in the year {data[2]} and handed over to {data[3]} in {data[4]}')



# adding a item to a list

fruits = ['mango', 'apple', 'orange']

# adding a fruit to a list
fruits.append('cherry')
print(fruits)

# inserting a new fruit to the list specify the position
fruits.insert(2, 'guava')
print(fruits)

# changing what is inside a list items
fruits[1] = 'udara'
print(fruits)

# removing a fruit from a list
fruits.remove('orange')
print(fruits)

# use pop to remove the last item in a list
fruits.pop()
print(fruits)

# use pop to remove a item from a list with specification
fruits.pop(1)
print(fruits)


# knowing the number of items in a list
print(len(fruits))

# for deleting
# del fruits 


