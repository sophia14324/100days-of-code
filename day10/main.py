import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # number of attempts allowed
    max_attempts = 5
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Take a guess: "))
            
            # Increment the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            # Provide a hint after a wrong guess
            if attempts < max_attempts:
                print("You have", max_attempts - attempts, "attempts remaining.")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # If the player couldn't guess the number within the allowed attempts
    if attempts == max_attempts and guess != secret_number:
        print("Sorry, you've run out of attempts. The secret number was:", secret_number)

if __name__ == "__main__":
    guess_the_number()
