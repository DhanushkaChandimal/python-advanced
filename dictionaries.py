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



# # Adding, Modifying, and Removing Elements
# Adding Elements:
print(my_dict)
my_dict['profession'] = 'Engineer'
print(my_dict)

# Modifying Elements:
my_dict['profession'] = 'Changed profession'
print(my_dict)

# Removing Elements:
del my_dict['profession']
print(my_dict)

removed_value = my_dict.pop(1)
print(removed_value)  # Output: 777777
print(my_dict)
removed_value = my_dict.pop(1, "There is no key with ypour input")
print(removed_value)  # Output: 777777
print(my_dict)