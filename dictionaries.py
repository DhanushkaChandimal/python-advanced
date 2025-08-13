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



# # Dictionary Methods
# .keys():
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(list(my_dict.keys()))  # Output: ['name', 'age', 'city']
for key in my_dict.keys():
    print(key)
    
# .values():
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])
print(list(my_dict.values()))  # Output: ['Alice', 25, 'New York']
for value in my_dict.values():
    print(value)

# .items():
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 25), ('city', 'New York')]
for key, value in my_dict.items():
    print(f"Key \"{key}\" holds \"{value}\" value")

# # Looping Through Dictionaries
# Looping through Keys Only:
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# Looping through Values Only:
for value in my_dict.values():
    print(value)

# Looping through Key-Value Pairs:
for key, value in my_dict.items():
    print(f"{key}: {value}")



# # Nested Dictionaries
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

city_user1 = users['user1']['address']['city']
print(city_user1)  # Output: New York
print(users)
for user, info in users.items():
    print(f"User ID: {user}")
    for key, value in info.items():
        print(f"  {key}: {value}")



# # A List of Dictionaries
students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]
first_student_major = students[0]['major']
print(first_student_major)  # Output: Physics
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")



# # A List within a Dictionary
favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}
alice_books = favorite_books['Alice']
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

second_favorite_bob = favorite_books['Bob'][1]
print(second_favorite_bob)  # Output: Catch-22

for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")