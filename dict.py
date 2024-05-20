blank_dict = {}
print(blank_dict)
print(type(blank_dict))
print()
print()

# Dictionary - must have key:value pairs
phone_book = {
    "Howard" : "888-297-3502",
    "Hubbard" : "222-484-9751",
    "Haskins" : "999-574-3251",
    "Hopkins" : "444-328-9191",
    "Honeycut" : "333-285-6731"
}
# This prints the dictionary in alphabetical order
# Note that the {key} prompts the key, but in the [key], the value is being called
for key in sorted(phone_book.keys()):
    print(f"{key} --> {phone_book[key]}")
print()

# Accessing data from dictionary using key - voice ai can be used to call the key and the number appear or dial
print(phone_book["Hubbard"])
print()

# Storing values from dictionary in a different variable
numbers = phone_book["Haskins"]
print(numbers)