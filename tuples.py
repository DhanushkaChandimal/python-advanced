# Ordered: The items in a tuple are indexed starting from 0.
# Immutable: You cannot change, add, or remove elements once the tuple is created.
# Heterogeneous: You can mix different data types in the same tuple.

my_tuple = (1, 2, 3,"string", ("another tuple", 2, 3))
print(my_tuple)
print(my_tuple[0])

## Creating a Tuple

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


