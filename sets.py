# # Unordered: You won’t know the order of elements.
# # Mutable: You can change the set’s contents by adding or removing items.
# # Unique: Sets automatically remove duplicate items.
# # No Indexing: Unlike lists or tuples, sets don't have a defined order, so you can't access items using an index.

# # Creating an Empty Set
# empty_set = set()
# print(type(empty_set))

# # Creating a Set with Values
# new_set = {"one", 2, "three"}
# print(new_set)

# # Convert a list into a set to eliminate duplicate values
# alist = ['item', 'item', 'stuff', 'thing', 'oddity']
# set_list = set(alist)
# print(alist)
# print(set_list)

# # Looping Over a Set
# with open("printing_list.txt", "w") as file:
#     for item in set_list:
#         print(item)
#         file.write(item + "\n")



# ## Set Methods

# # Checking Membership
# my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
# print("superman" in my_set)
# print("SUPERMAN" in my_set)

# # Adding Items to a Set
# my_set.add("green lantern")
# my_set.add("superman") # Just ignore without any message
# print(my_set)

# # Subset and Superset Checks
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))



# Set Operations

# Union
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set_union = set1.union(set2)
print(set_union)

# Intersection
set_intersection = set1.intersection(set2)
print(set_intersection)
print({1,2,3}.intersection({4,5,6}))

# Diffference
print(set1.difference(set2)) # {1, 2}
print(set2.difference(set1)) # {6, 7}

# Symmetric difference
print(set1.symmetric_difference(set2)) # {1, 2, 6, 7}
print(set2.symmetric_difference(set1)) # {1, 2, 6, 7}


# Exercise
def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    print("Unique emails in list 1: ", set1)
    print("Unique emails in list 2: ", set2)

    print("All Unique emails: ", set1.union(set2))
    
    print("Emails exist in both lists: ", set1.intersection(set2))
    print("Emails that are unique to each list: ", set1.symmetric_difference(set2))

email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)