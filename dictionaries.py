# Dict - collection of items - mutable - uordered - not indexed - keyed = key/value pairs, keys cannot have duplicates

person1 = {
    "name": "Dee",
    "last_name": "Otieno",
    "age": 47
}

# print(person1['age']) # accessing a key option 1
# print(person1.get('name'))  # option 2
# print(person1.get('foo', 'Key not found'))

# person1["address"] = 'Melbourne' # adding k/v
# # person1["suburb"] = 'Oakleigh'
# # person1["village"] = 'Greens'
person1["address"] = {'state': "QLD", "postcode": 2000} # making the value a dict
# print(type(person1))
print(person1['address']['postcode'])
print(person1)
person1.update({'name': 'Tom:', 'age': 50})
print(person1)

# Loop
# for key in person1: 
#     print(f'Key: {key}')
#     print(f'Value: {person1[key]}')

# same as above
for key, val in person1.items(): 
    print(f'Key: {key}')
    print(f'Value: {val}')

