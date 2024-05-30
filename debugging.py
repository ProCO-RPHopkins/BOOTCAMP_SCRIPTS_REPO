
# Zero Division Error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")
print()

# Value Error
try:
    number = int("invalid_number")
except ValueError as e:
    print(f"A ValueError occured: {e}")
print()

# File not found error
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
print()

# Type Error
try:
    result = "hello" + 42
except TypeError:
    print("Cannot concatenate string and integer")

# Index Error
try:
    my_list = [1, 2, 3]
    value = my_list[10]
except IndexError:
    print("Index out of range")

# Key Error
try:
    my_dict = {"name": "Alice", "age": 30}
    value = my_dict["city"]
except KeyError:
    print("Key not found in dictionary")

# Catching multiple exceptions (Both type errors and index errors)
'''Note that when run, it will only do the first error and when that is
fixed, it will move into the next error'''
try:
    # Example 1: TypeError
    value = "hello" + 42  # This will raise a TypeError

    # Example 2: IndexError
    my_list = [1, 2, 3]
    element = my_list[10]  # This will raise an IndexError
except TypeError:
    print("Caught a TypeError: Cannot concatenate string and integer")
except IndexError:
    print("Caught an IndexError: Index out of range")


# Provides for any error
try:
    # Some code that may raise an exception
    result = 1 / 0  # This will raise a ZeroDivisionError
    # ... other code that might raise exceptions ...
except:
    print("An exception occurred!")

# Rest of your program
print("Continuing execution after exception")


# Try, except, else for ZeroDivisionError
try:
    x = 10
    y = 0
    z = x / y  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print(f"Result: {z}")  # This line will execute if no exception occurs

'''# Try, except, finally block that attempts to read a file and
prints a message indicating that resources are being cleaned up'''
try:
    # Attempt to open and read a file
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("File not found or cannot be opened.")
finally:
    print("Cleaning up resources... File is closed.")


# Making a try, except statement pass
try:
    num = int("hello")
except ValueError:
    pass

# Dropped in Slack as an exercise
def watch_recent_films(start_index, end_index):
    recent_films = [“Hidden Figures”, “Dune”, “Alien”, “Shrek”]
    selected_films = recent_films[start_index:end_index]
    if not selected_films:
        print(“Error: Film index is out of range.“)
        return
    print(“\nNow watching:“)
    for film in selected_films:
        print(film)
# Test cases
watch_recent_
watch_recent_films(-4, -1)





