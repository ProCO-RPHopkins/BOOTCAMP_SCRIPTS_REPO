# Key operators

x = 5
y = 10
print(x > y)
print( x == 5)
print()
print()

a = 4
b = 8.25
c = "a"
d = "A"
e = "Ryan"

print(a < b)
print(a > 5)

# ASCII values
print(c == d)
print(c > d)
print(e == "Ryan")
print(e == "ryan")
print()
print()

# Combining conditions
a = 10
b = 20
print(a < 5 and b < 25)
print(not(a > 15)) # output true
print()
print()

a = 50
b = 100

print(a > 30 and b < 101) # true
print(a < 40 or b < 90) # false 
print(a != 10 or b == 150) # true
print(not(a == 50)) # false
print()
print()

# Conditional Statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
print()
print()

name = str(input("Enter your name: "))

if len(name) <= 10:
    print("You have a short name")
elif len(name) <=15:
    print("You have a average length name")
else:
    print("Your name is long")
# Nested loops
score = 30
if score > 50:
    print("You passed")
    if score > 90:
        print("Good job!")
    elif score > 70:
        print("Try harder next time")
    else:
        print("Try harder next time")
else:
    print("You failed!")
print()
print()


name = input("What is your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter your name.")


# Nested conditional statements
age = 19
parental_consent = False

if age < 18:
    if parental_consent:
        print("You are allowed to participate")
    else:
        print("You are not allowed to participate without parental control")
else:
    print("You are allowed to participate")

print(bool(0))

print("hello" == 'hello')
