py_list = [1, 2, 3, 4, 5] # indexed, ordered, changeable, and allow duplicate values.
py_tuple = (1, 2, 3, 4, 5) # indexed, ordered, unchangeable, and allow duplicate values.
py_set = {1, 2, 3, 4, 5} # unindexed, unordered, changeable, and do not allow duplicate values.
py_dict = {'a': 1, 'b': 2, 'c': 3} # key-value pairs, ordered (as of Python 3.7), changeable, and do not allow duplicate keys.

# Print the data structures
print("List:", py_list)
print("Tuple:", py_tuple)
print("Set:", py_set)
print("Dictionary:", py_dict)

# Accessing elements
print("First element of list:", py_list[0])
print("First element of tuple:", py_tuple[0])
print("Accessing value for key 'a' in dictionary:", py_dict['a'])
print("Set contains 3:", 3 in py_set)

# Modifying elements
py_list[0] = 10
print("Modified list:", py_list)
# py_tuple[0] = 10 # This will raise an error since tuples are unchangeable
py_set.add(6)
print("Modified set:", py_set)
py_dict['d'] = 4
print("Modified dictionary:", py_dict)

# Demonstrating duplicate values
py_list.append(2)
print("List with duplicate value:", py_list)
# py_set.add(3) # This will not change the set since 3 is already present
print("Set after attempting to add duplicate value:", py_set)
