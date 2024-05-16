# Lists inside [square brackets]
# Dictionaries use {squiggly brackets}
# Remember lists begin at index 0
my_list = [1, 2, "hello", True, 3.14]
print(my_list)
print()

# Append lists
shopping_list = ["apple", "eggs", "bread", "milk"]
print("Initial Shopping List: ", shopping_list)
shopping_list.append("peanut butter")
print(shopping_list)
print()

# Remove from list
shopping_list.remove("bread")
print("New Shopping List: ", shopping_list)
print()

# Popped from list
popped_item = shopping_list.pop(2)
print("Popped Item:", popped_item)
print("New Shopping List:", shopping_list)
print()

shopping_list.append("Soda")
print("Appended list:", shopping_list)
print()

num_items = len(shopping_list)
print("Number of items in the list:", num_items)

# Access individual items
tool_list = ["hammer", "screw gun", "drill", "ladder", "saw", "tool box", "electric sander"]
index_finder = tool_list[4]
print(tool_list)
print("Saw:", index_finder)

# Slicing Lists 
# Doesn't include the last index (e.g., 1:3 would give 1 index and 2 index)
tool_list = ["hammer", "screw gun", "drill", "ladder", "saw", "tool box", "electric sander"]
subset_list = tool_list[2:5]
print(tool_list)
print(subset_list)
print()
print()
print()

# Using different mutable list approaches
tool_list = ["hammer", "screw gun", "drill", "ladder", "saw", "tool box", "electric sander"]
print(tool_list)

tool_list.append("motorcycle")
print("Appended List", tool_list)

remove_item = tool_list.remove("hammer")
print("Removed hammer from list:", tool_list)

pop_tool = tool_list.pop(4)
print(tool_list)
print("The popped item is tool box:", pop_tool)
print()

slice_list = tool_list[2:4]
print(tool_list)
print("The sliced list contains ladder and saw:", slice_list)
# double colon for every other element
every_other = tool_list[::2]
print(every_other)
print()
print()


# Separates elements of the word with split() function
sentence = "This is a sentence."
word_list = sentence.split()
print("List of Words", word_list)

new_sentence = "".join(word_list)
print("Joined sentence, no space", new_sentence)
print()

# For loop - iterates till the end of list and then stops
shoppers_list = ["apples", "oranges", "dog", "cat", "feline", "mouse"]
print("Shoppers List:")
for item in shoppers_list:
    print("*"+item+"*")
    # I can use either the one above or the one below
    print(f"I need 5 {item}.")



