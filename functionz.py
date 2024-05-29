# Functions help organize code, make it more readable, and don't repeat yourself (DRY)
# Function is a block of reusable code

def greet():
    print("Hello, welcome to my code interface!")
    # Nothing happens because the function was not called

# Below calls the function
greet ()
print()

# Area of a rectangle
def rec_area(l, w):
    return l * w
print(rec_area(10, 4))

# Flexible parameters
def greet_with_name(name): # 'name' is a parameter
    print(f"Hello {name}!")

greet_with_name("Ryan") # "Ryan" is an argument
greet_with_name("Becci") # "Becci" is an argument
print()

def add(a, b):
    '''This function takes two numbers and returns their sum'''
    return a + b
help(add) # Returns the note


def select_movie(movie):
    print(f"select movie: {movie}")

    films = ["The Book of Clarence", "Dune", "Batman"]
    for movie in films: # Films is the defined variable in the 'in' statement 
        select_movie(movie) # The parameter in this has to be the same as the 'for' statement
        print(f"Now watching: {movie}")
        print()

    print("Finished watching recent films. Now lets watch a random movie.")
print(select_movie)


def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)
print()



def test_scope():
    local_var = " I am a local"
    print()
    print

def outer_function(): 
    def inner_function():
        print("This is an inner function")
    inner_function()

outer_function()

def watch_recent_films():
    def watch_movie():
        print("open streaming service")
        print("select movie")
        print("press play")

    recent_films = ["the book", "dune", "superman"]
    for film in recent_films:
        watch_movie()
        print(f"Now watching: {film}")
        print()

watch_recent_films()
print()


add = lambda a, b,: a + b # Can use this for strings (i.e., var = lambada film: print(f"Just finished
                                                        # watching {film}!")
print(add(5, 3))  
print()

def main():
    print("This is the main function")

if __name__ == "__main__":
    main()