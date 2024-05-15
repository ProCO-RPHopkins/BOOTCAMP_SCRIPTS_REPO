name = 'MS Student'

# When I used commas instead of "+", it left a weird space
print("Hi, my name is, " + name + '.')

# This is another option that is easier
print(f"Hi, my name is {name}.")
print()

# String methods
print("Hi, I'm really excited to be here :)".upper())
print("Hi, I'm feeling a bit under the weather today :(".lower())

# Replace
password_info = "don't FORGET, the password is 1234"
print(password_info)
print(password_info.replace('1234', "sensitive info".upper()))

sentence = "Let's try something different"
count_es = sentence.count("e")
print(count_es)
print()

# type() function allows to identify classes
print(type('7'), type(7), type(7.0))


# Conversions from int to str to float
int_var = 9
var_as_string = str(int_var)
var_as_float = float(int_var)

print(f"int_var:{type(int_var)}")
print(f"int_var:{type(var_as_string)}")
print(f"int_var:{type(var_as_float)}")