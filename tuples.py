# Ordered: The items in a tuple are indexed starting from 0.
# Immutable: You cannot change, add, or remove elements once the tuple is created.
# Heterogeneous: You can mix different data types in the same tuple.

my_tuple = (1, 2, 3,"string", ("another tuple", 2, 3))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

# # Creating a Tuple

# Using parentheses ()
tuple1 = (10, "Python", 3.14)

# Without parentheses (tuple packing):
tuple2 = 10, "Python", 3.14

# Single-element tuples (important!):
single_element_tuple = (5,)

# Empty tuples:
empty_tuple = ()

# Using the tuple() constructor:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)



# # Tuple Manipulation

# Accessing Tuple Elements
my_tuple = ("apple", [1, 2, (11, 12, {"Set", "wow", 1})])
print(my_tuple[0])
print(my_tuple[1][2][2])

# Slicing Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Looping over Tuples
for num in my_tuple: 
	print(num) 

# Tuple Immutability
# my_tuple[1] = 40  # Error! Tuples cannot be changed
print("Before change: ", my_tuple)
my_list = list(my_tuple)
my_list[1] = 40
my_tuple = tuple(my_list)
print("After change: ", my_tuple)



# # Packing and Unpacking Tuples
# Tuple Packing
person_info = "Alice", 30, "Developer"

# Tuple Unpacking
name, age, profession = person_info
print(name)
print(age)
print(profession)

# Extended Unpacking
numbers = (1, 2, 3, 4, 5)
first, *rest, last = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4]
print(last)   # Output: 5

# Ignoring Values with Underscore (_)
person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info  # Ignore age and location

print(name)       # Output: Eve
print(profession) # Output: Artist
