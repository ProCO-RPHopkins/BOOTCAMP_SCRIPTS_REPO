a = 2 + 2
b = 4

# Note that == is equal, or what is called a comparison operator
# The = is to assign a value to a variableg
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
print(True == 1) # True
print(False == 0) # True 
print(False != 1) # True
print(True >= 1.1) # False
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


# Logical operators
   # Or - At least one of the comparisons have to be true
print(5 != 7 or 4==4) # When one is true, the "or" statement is true
print(2 < 4 or 6 == 6) # When both are true the "or" statement is true
print(7 > 9 or 5 + 2 == 8) # This one is false becaause neither are true
print()

   # And - Both of the comparisons have to be true
print(5 * 2 < 100 / 5 and 3 ** 3 == 27) # Both statements are true, so the "and" expression is true
print(2 * 3 == 6 and 2 + 5 < 4) # One statement is true, so the "and" expression is false
print()

   # This is cool - can run an "and" plus "or" expression on the same print line
print(5 == 2 + 3 and 4 * 3 != 13, 9 > 10 or 3 <= 4) # True True
print()

   # Boolean logic expressions
print(False and False) # Generates a False statement
print(True and True) # Generates a True statement
print(False and True) # Generates a False statement
print(False or True) # This generates a True statement
print(True or True) # This generates a True statement
print(False or False) # This generates a False statement
print()

   # Not - Reverse whatever Boolean value is produced by a logical expression
print(not 2 < 3) # Not reverses this True statement to a False Statement
print(not True) # False
print(not 5 != 6) # False
print(not 3 * 2 == 7) # Not reverses this False statement to True
print(not False) # True
print()
