import random

def choose_random_name(names):
    return random.choice(names)

if __name__ == "__main__":
    names = ["Kevin B.", "Anthony P.", "Naima H.", "Ryan P."]
    random_name = choose_random_name(names)
    print(f"The randomly chose name is: {random_name}")

# Import an entire module
import math
print(math.sqrt(16))

# Import a specific function from a module
from math import sqrt
print(sqrt(16))

# import a module with an alias
import math as m
print(m.sqrt(16))

from transfer_file import greet, add

result = add()
print(greet("Ryan"))
print("The sum is: ", result)

