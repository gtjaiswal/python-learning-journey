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

# --- Using range() in for loops ---

print("\n# --- Using range() in for loops ---")

# 1. range(stop): Generates numbers from 0 up to (but not including) stop.
print("\n# 1. range(stop)")
print("Looping from 0 to 4:")
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print("\n")

# 2. range(start, stop): Generates numbers from start up to (but not including) stop.
print("# 2. range(start, stop)")
print("Looping from 2 to 5:")
for i in range(2, 6):
    print(i, end=" ")  # Output: 2 3 4 5
print("\n")

# 3. range(start, stop, step): Generates numbers from start to stop, with a step.
print("# 3. range(start, stop, step)")
print("Looping from 0 to 10 with a step of 2:")
for i in range(0, 11, 2):
    print(i, end=" ")  # Output: 0 2 4 6 8 10
print("\n")

# Looping backwards with a negative step
print("Looping backwards from 5 to 1:")
for i in range(5, 0, -1):
    print(i, end=" ")  # Output: 5 4 3 2 1
print("\n")

# Common use case: Iterating over a list by index
print("Using range to iterate over a list by index:")
my_list = ['a', 'b', 'c', 'd']
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")
print()

# --- Adding to a Dictionary ---

print("\n# --- Adding to a Dictionary ---")

# 1. Using square bracket [] syntax
print("\n# 1. Using square bracket [] syntax")
my_dict_add = {'name': 'Alice', 'age': 30}
print("Original dictionary:", my_dict_add)
# Add a new key-value pair
my_dict_add['city'] = 'New York'
print("After adding 'city':", my_dict_add)
# Update an existing key
my_dict_add['age'] = 31
print("After updating 'age':", my_dict_add)
print()

# 2. Using the update() method
print("# 2. Using the update() method")
# Add multiple items from another dictionary
my_dict_add.update({'country': 'USA', 'occupation': 'Engineer'})
print("After update() with another dict:", my_dict_add)
# You can also update from a list of tuples
my_dict_add.update([('zipcode', 10001), ('status', 'active')])
print("After update() with a list of tuples:", my_dict_add)
print()

# --- Getting Dictionary Keys ---

print("\n# --- Getting Dictionary Keys ---")
my_dict_keys = {'name': 'Bob', 'age': 42, 'city': 'London'}
print(f"Original dictionary: {my_dict_keys}\n")

# The .keys() method returns a "view" of the dictionary's keys
keys_view = my_dict_keys.keys()
print(f"Keys view object: {keys_view}")

# Iterating directly over the dictionary (or its .keys() view) is the most common way to use keys
print("\nIterating over keys:")
for key in my_dict_keys:
    print(f"- The key is '{key}' and its value is '{my_dict_keys[key]}'")

# To get a static list of keys, you can use the list() constructor
key_list = list(my_dict_keys.keys())
print(f"\nStatic list of keys: {key_list}")
print()

# --- Sorting a Dictionary ---

print("\n# --- Sorting a Dictionary ---")
my_dict_sort = {'banana': 3, 'apple': 5, 'cherry': 1, 'date': 2}
print(f"Original dictionary: {my_dict_sort}")

# 1. Sorting by Keys
# sorted() returns a list of keys sorted alphabetically
sorted_keys = sorted(my_dict_sort)
# Create a new dictionary based on sorted keys
sorted_by_keys = {k: my_dict_sort[k] for k in sorted_keys}
print(f"Sorted by keys: {sorted_by_keys}")

# 2. Sorting by Values
# Use sorted() on items(), specifying the value (item[1]) as the sort key
sorted_items = sorted(my_dict_sort.items(), key=lambda item: item[1])
sorted_by_values = dict(sorted_items)
print(f"Sorted by values: {sorted_by_values}")

# 3. Sorting by Values (Reverse)
sorted_items_desc = sorted(my_dict_sort.items(), key=lambda item: item[1], reverse=True)
sorted_by_values_desc = dict(sorted_items_desc)
print(f"Sorted by values (descending): {sorted_by_values_desc}")
print()

# --- Using Multiple Indices/Variables in Loops ---

print("\n# --- Using Multiple Indices/Variables in Loops ---")

# 1. Nested Loops (Iterating over pairs)
# Useful for comparing every element with every other element (O(n^2))
print("\n# 1. Nested Loops (Pairs)")
nums = [10, 20, 30]
print(f"List: {nums}")
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(f"Pair indices ({i}, {j}) -> Values ({nums[i]}, {nums[j]})")

# 2. Using zip() to iterate over two lists simultaneously
print("\n# 2. Using zip() (Parallel Iteration)")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 3. Using enumerate() to get index and value
print("\n# 3. Using enumerate() (Index and Value)")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print()
