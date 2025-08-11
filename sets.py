# Unordered: You won’t know the order of elements.
# Mutable: You can change the set’s contents by adding or removing items.
# Unique: Sets automatically remove duplicate items.
# No Indexing: Unlike lists or tuples, sets don't have a defined order, so you can't access items using an index.

# Creating an Empty Set
empty_set = set()
print(type(empty_set))

# Creating a Set with Values
new_set = {"one", 2, "three"}
print(new_set)

# Convert a list into a set to eliminate duplicate values
alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)
print(alist)
print(set_list)

# Looping Over a Set
with open("printing_list.txt", "w") as file:
    for item in set_list:
        print(item)
        file.write(item + "\n")

# Set Methods


