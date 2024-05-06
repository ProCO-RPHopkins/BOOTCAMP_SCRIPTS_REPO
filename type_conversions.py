a = 'hi'
b = 2
c = 2.0
d = True

print(f'a: {type(a)}')
print(f'b: {type(b)}')
print(f'c: {type(c)}')
print(f'd: {type(d)}')

# str()
my_string1 = str(2)
my_string2 = str(2.7)
print(my_string1)
print(my_string2)
print(type(my_string1))
print(type(my_string2))
print()

# Convert string into a float
my_string3 = '2.5'
my_float = float(my_string3)
print(my_float)
print(type(my_float))
print()

# Convert strint into an integer
# String has to be a whole number. A decimal will throw an error
my_string4 = '2'
my_int = int(my_string4)
print(my_int)
print(type(my_int))
print()