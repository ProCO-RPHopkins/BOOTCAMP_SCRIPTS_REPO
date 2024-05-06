a = 2 + 2
b = 4

# Note that == is equal, or what is called a comparison operator
# The = is to assign a value to a variable
print()
print(a == b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)
print(a != b) # != is not equal
print()

print(a == 4)
print(a > 3)
print(a >= 5)
print(a >= 4)
print()

print(b == 5)
print(b <= 4)
print(b < 8)
print(b > 5)
print()

# Added a third variable
c = 12
print(a * 2 + b == c)
print(a * 3 + b != c)
print(a * 3 + b == c)
print()

# Binary True (==1) and False (==0)
print(True == 1)
print(False == 0)
print(False != 1)
print(True >= 1.1)
print()

# Comparison operators with strings 
# Python has case sensitivity, so upper case would not equal lower case strings

a = 'cat'
b = 'cat'
c = 'CAT'
print(a == b != c)
print(a > c) # This statement comes back True because lowercase values are greater in Unicode Standard
             # If I know Unicode values, 
                # could I use different words and they come back equal as long as the values are the same?             
print()