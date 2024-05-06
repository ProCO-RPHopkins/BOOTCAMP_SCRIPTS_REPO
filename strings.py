street = 'Cushing Road'
print(street)
print()
 
# Using an escape character (i.e., \), I can move a long line into multiple lines without breaking the string
# Notice that the indented lines leave a bigger space between text
lyrics = "Telling myself I won't go there \
    Oh, but I know that I won't care \
    Tryna wash away all the blood I've spilt \
This lust is a burden that we both share \
Two sinners can't atone from a lone prayer \
Souls tied, intertwined by our pride and guilt.\n"
print(lyrics)

# Using another escape character (i.e., line break: \n), starts a new paragraph when I run the script
# I can use the line break at the end rather than "print()" to create a space
lyrics2 = "Telling myself I won't go there \
\nOh, but I know that I won't care \
\nTryna wash away all the blood I've spilt \
\nThis lust is a burden that we both share \
\nTwo sinners can't atone from a lone prayer \
\nSouls tied, intertwined by our pride and guilt.\n"
print(lyrics2)

# Add a tabbed space using "\t"
lyrics3 = "Telling myself I won't go there \
\n\tOh, but I know that I won't care \
\n\tTryna wash away all the blood I've spilt \
\nThis lust is a burden that we both share \
\n\tTwo sinners can't atone from a lone prayer \
\n\tSouls tied, intertwined by our pride and guilt.\n"
print(lyrics3)

# Creating an F-string to join variable value within the string
profit = 120
my_f_string = f'My profit today is ${profit + profit}\n'
print(my_f_string)

# Rather than assigning variables, I can just "print()" the F-string statement
print(f'If I earn $120 a day, \
five days a week, \
and my apartment cost $200 a week, \
I have a profit of ${120 * 5 - 200} a week\n')

# Concatenation of strings
fruit1 = 'apple'
fruit2 = 'banana'
# Fruit3 will cocatenate fruit1 and fruit2
fruit3 = fruit1 + ' ' + fruit2
print(fruit3)
print()

# Can also cocatenate in the "print()" statement rather than writing another variable to cocatenate
first_name = 'Ryan\n'
middle_name = 'Patrick\n'
last_name = 'Hopkins\n'
print(first_name + middle_name + last_name)

# Strings upper and lower
firstname = 'Ryan'
lastname = 'HOPKINS'
print(firstname.upper() + ' ' + lastname.lower())
print()