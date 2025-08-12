my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    1: 25,
    1: 34,
    1: 56,
    1: 444,
    1: 777777,
}

print(my_dict) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 1: 777777}

# Accessing Values in a Dictionary
print(my_dict['name'])  # Output: Alice
# print(my_dict['ads'])  # KeyError: 'ads'

# The .get() method & avoiding missing keys 
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('ads'))  # Output: None
