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

# There are 11 total list methods
#   1. append
#   2. clear
#   3. copy
#   4. count
#   5. extend
#   6. index
#   7. insert
#   8. pop 
#   9. remove
#  10. reverse
#  11. sort

homework_list = ['journal', 'discussion post', 'discussion response', 'paper']
homework_list.append('#appended list') # append can only take one argument
print(homework_list)
print()

# This is another way to create variables and str lists
jobs: list[str] = ['electrician', 'plumber', 'electrician', 'HVAC technician']
jobs.append('mechanic')

# jobs.clear()  # clears the list
jobs_addition: list[str] = ['corn', 'plumb', 'pear']
copy_jobs: list[str] = jobs.copy()
electricians = jobs.count('electrician') # counts the number of occurences: In this case 2
popped = jobs.pop(1) # If I don't add an index number, it will remove the last on the list

copy_jobs.remove('HVAC technician')
jobs.extend(jobs_addition) # add brackets to put list inside of list. Ex: jobs.extend([jobs_addition])
jobs.insert(6, 'tractor') # Inserts it to the place number. Notice that 'plum' is +1 on the index (i.e., 7)
jobs.remove('electrician') # Only removes one instance. Can only take one argument
jobs.reverse() # reverses list. Notice the index number of 'plumb' changed from 5 to 2 with reversed list
jobs.sort(key=lambda professions: professions.lower()) # automatically goes in alphabetical order
          # The 'key' here places HVAC in alphabetical order as if 'HVAC' were lowercase.
                # Otherwise uppercase would be at beginning of list
                # Could create a key based on word length. Ex: jobs.sort(key=lambda professions: len(professions))
print(jobs)
print(copy_jobs)
print(electricians)
print(jobs)
print(jobs.index('plumb')) # shows place value. Remember, index starts at 0
print(jobs)
print(popped)
print(jobs)
print(jobs)

dog_list = ['pit', 'shepherd', 'bulldog', 'doberman']
print(len(dog_list))