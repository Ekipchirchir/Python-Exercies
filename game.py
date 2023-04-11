import random

def main():
    # Prompt the user for the level
    level = get_level()
    
    # Generate a random number within the given level range
    number = generate_number(level)
    
    # Prompt the user to guess the number
    while True:
        guess = input("Guess a number between 1 and {}: ".format(level))
        
        # Validate the user's guess
        if not guess.isdigit():
            print("Please enter a positive integer.")
            continue
        
        guess = int(guess)
        if guess < 1 or guess > level:
            print("Please enter a number between 1 and {}.".format(level))
            continue
        
        # Check if the user's guess is correct
        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        else:
            print("Too large!")
    
def get_level():
    """
    Prompts the user for a level and returns a positive integer.
    """
    while True:
        level = input("Enter a positive integer for the level: ")
        if level.isdigit():
            return int(level)
        else:
            print("Please enter a positive integer.")

def generate_number(level):
    """
    Returns a random integer between 1 and the given level, inclusive.
    """
    return random.randint(1, level)

if __name__ == "__main__":
    main()