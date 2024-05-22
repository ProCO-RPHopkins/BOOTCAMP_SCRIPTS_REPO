# Import the random module
import random

# Initialize the score to 0
import random 
score = 0
# Define function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False # Numbers less than or equalt to one are not prime not numbers
    for i in range(2, int(n**0.5) + 1): # n**0.5 is a mathematical test for exponents
        if n % i == 0: # If there is no remainder (i.e., 0), the number isn't prime
            return False # If no divisors found, n is prime
    return True

while True:
  
  number = random.randint(1, 100)  # Generate a random number between 1 and 100
  print(f"Is {number} a prime number? (yes/no)")
  user_input = input().strip().lower()  # Get user input and convert it to lowercase

  if user_input not in ['yes', 'no']:
    print("Please answer with 'yes' or 'no'.")
    continue # Ask again if the input is not valid/ reloops if invalid input
  
  guess_is_prime = user_input == 'yes'  # Convert user's guess to a boolean
  actual_is_prime = is_prime(number)  # Check if the number is actually prime
  if guess_is_prime == actual_is_prime:
    print("Correct!")  # User guessed correctly
    score += 1  # Increment score
  else:
    print("Incorrect.")  # User guessed incorrectly
    
  print(f"Your current score is: {score}")
  print("Do you want to play again? (yes/no)")

  play_again = input().strip().lower()  # Ask the user if they want to play again
  if play_again != 'yes':
    break  # Exit the loop if the user doesn't want to play again
print(f"Thanks for playing! Your final score is: {score}")  # Print the final score
