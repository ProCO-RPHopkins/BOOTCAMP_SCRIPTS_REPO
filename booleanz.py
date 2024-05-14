#assign variable with description

length = 5
width = 8
area = length * width
print("The area of the rectangle is", area)
print()

# modifying variable: If variable changes below original variable, it will go with the one below
length = 20
area = length * width
print(area)
print()

#complex calculation using descriptive names
base_price = 100
discount_percentage = 20
final_price = base_price*(1-discount_percentage/100)
print(final_price)
print()

name = "Batman"
age = 25
print("My name is", name, "and I am", age, "years old.")