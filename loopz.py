# If repeating something three or more times, it might be best to throw in a loop.
a_list = [1, 3, 5]

for value in a_list:
    print(value)
    # print hello world each time it iterates through the list
    print("Hello, World!")
print("Done iterating through list.")
print()

# list of lowercase strings
lower_list = ["here", "are", "my", "lower", "case", "words"]

# a blank list for uppercase strings
upper_list = []

for i in lower_list:
    upper_list.append(i.upper())
    print(i) # The output for this is simply the lower_list
    print(upper_list) # Notice if I print upper_list inside the loop, every iteration appears
print()
print(upper_list) # If I print upper_list outside the loop, it simply capitalizes without the iteration
print()

for i in range(len(lower_list)): 
    print(f'The index is {i} and the element is {lower_list[i]}') # The [i] pulls out the element
                                                                # If I remove [i], it prints entire list
print()


# Looping through characters in a string
my_string = "ice cream"
vowels = ['a', 'e', 'i', 'o', 'u']
space = [" "]
# If I added different symbols, maybe I could create another varable NOT isalpha and give the space exception
for letter in my_string: # Note that "letter" in this for loop can be anything.
                            # Usually use the singular of the plural variable
    if letter in vowels:
        print(f'{letter} is a vowel') # This iterates through each letter
    elif letter in space:
        print(f'{letter} is a space')
    else:
        print(f'{letter} is not a vowel')
print()


# Using the range() function
for i in range(8): # Does not include last number of index because it begins at 0, so it is range 8
    print(i)
print()

'''While loop is similar to for loop, but it keeps iterating unless a "break" is added 
or a condition is met.''' 
count = 0
while (count <= 5):
    print(count)
    count = count + 1 # The +1 basically acts as an accumulator
print("The loop is done iterating")



