# Lists - A sequence of items
#         1) They are mutable meaning they can change by editing content (i.e., adding, removing, or replacing items)
#         2) Can assign update lists using variables
#         3) In lists, indices start at zero. So to replace the first item, the place value would be 0

grocery_list = ["apples", "pasta", "milk"]
print(grocery_list)
print()

integer_list = [1, 3, 4, 5]
print(integer_list)
print()

float_list = (1.74, 99.99, -0.23)
boolean_list = (True, False)
print(float_list, boolean_list)
print()

mixed_list = (1.74, True, 5, "apples")
print(mixed_list)
print()

item_1 = ("apples")
item_2 = ("pasta")
item_3 = ("milk")

grocery_list2 = [item_1, item_2, item_3]
print(grocery_list2)
print()

empty_list = []
print(empty_list)
print(type(empty_list))
print()

print(10 % 3) # Worry about this later - Just testing something
print()

# modify lists
    # length of list
integer_list2 = [1,2,3,4,5]
integer_length = len(integer_list2)
print(integer_length)
print()
# Another option is simply to use the print function with len & list rather than assigning variable (above)
print(len(integer_list2))
print(integer_list2)
print()

integer_list2.append(6)
print(integer_list2)
print(len(integer_list2))