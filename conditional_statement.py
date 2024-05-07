print()
# Conditional Statements
a = 5
if  a > 6: # type in logical expression after keyword 'if', which is known as a condition
    print('That is correct!') # This message prints out 'if' the expression is True, 4 or less
elif a == 3: 
    print('Got it on the second try!') # If I place a 5 on this line, then the expression is True...
    print()                               # and this message prints
        # Can have multiple elif statements. Also, can nest (indent) other 'if' statements
else: 
    print('Try again.') # If neither statements are true, then this message prints
    print()

while True:
    answer = input("Do you want to hear a joke? (press y / n) ")
    print()
    if answer == 'y':
        print("Then why don't you tell me one...HAHA") 
        print()
        break # exit the loop if 'y' is chosen
    elif answer == 'n':
        print("You're no fun.")
        print()
        break # exit the loop if 'n' is chosen
    else:
        print("That was not a valid response. Please enter 'y' or 'n'.")
        print()
    