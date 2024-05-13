# Indexing begins at 0, so when I print 2, it will give me the third element
names = ['Jane', 'John', 'Ryan', 'Julie', 'Jolene']

print(names[2])

# Replacing elements in the list using indices

names[2] = "Jack"
print(names[2])
print(names)
print()

# When starting from the back of the list, index numbers begin with -1, -2, -3, etc.
print(names[-2])
print()

# This will print error "out of range" because the total number of elements 
# doesn't match the indices because it starts at 0 (e.g., below)
    #   print(names[len(names)])

# This does not print an error and returns the first element because it is the full length in reverse
print(names[-len(names)])
print()

# Below returns the last element in the lenght; -1 modifies it to run the whole length without an error
print(names[len(names)-1])
print()

# List slicing - Note that it does not print end of list. 
# To get the end of the list, I need index 5 or higher, or nothing after colon
new_list = names[1:4]
print(new_list)

# Since I created a new list by slicing, the new list has a different name at index 0
print(new_list[0])

# Remember index begins at 0, and does not print the last index. To print entire list, use 3 for index 2
print(new_list[:3]) 