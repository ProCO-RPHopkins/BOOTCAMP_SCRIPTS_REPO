# Dictionaries
# Note key-values (separated by :) and not index (separted by ,)
my_dict = {"name": "Alice", "age": 25, "city": "New York", "email": "ryan.hopkins@maine.edu"}
my_dict["email"] = "ryan.hopkins2@snhu.edu" # This adds to the dictionary or it can replace if existing
print(my_dict["name"])  # Outputs: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict["age"])
print(my_dict["email"])
del my_dict["age"]
print(my_dict)
print()

values = my_dict["name"]
for key in my_dict:
    print(key) # key is a built in function to return key

for value in values: # Why is this iterating five times? It's iterating the len of name, 
                        # but it's the full name because I used values instead of value as the print variable
    print(values) # value is a built in function to return value
print()

for value in values: # This iterates one letter at a time
    print(value)
print()
print()



my_list = ["alice", "25" "New York"] # lists use [], dictionaries use {}, and tuples use ()
print(my_list[0]) # Note that in lists, I can use the index to call an element in the list
# chris = {"name": "Chris", "age": 30, "city": "LA"}
# dani = {"name": "Dani", "age": 25, "city": "New York"}

# Tuples - Elements have a specific order, they're immutable, and elements can be duplicated
my_tuple = ("Alice", 25, "New York")
print(my_tuple[2])
print()
# users = [alice, chris, dani] # This simply adds users in a list to use
# print(users)

# for user in users:
#     print(user["name"])
#     print(user["age"])
#     print(user["city"])

book = {
    "title" : "Running Man",
    "author" : "Jackson",
    "year" : 1995,
    "publisher" : "O'Hare"
}
print(book)
print()
book["pages"] = 200 # adds key and value
book["year"] = 2004 # changes value in key name "year"
print(book)
print()

book.update({"year": 9000}) # Update is a built in function to change
print(book)
print()

del book["year"]
print(book)
print()

for key, value in book.items():  # Another way to run this with built in function
    print(f"{key}: {value}")

print()
