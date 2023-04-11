import random


def main():
    # prompt the user for a level and get the integer representation
    level = get_level()

    # initialize variables for the score and current problem number
    score = 0
    problem_num = 1

    # loop through generating and prompting for 10 math problems
    for i in range(10):
        # generate random integers for the problem
        x = generate_integer(level)
        y = generate_integer(level)

        # prompt the user for the answer
        prompt = str(x) + " + " + str(y) + " = "
        answer = input(prompt)

        # keep track of the number of tries
        num_tries = 1

        # loop until the user enters the correct answer or exceeds the maximum number of tries
        while answer != str(x + y) and num_tries < 3:
            # output EEE for incorrect answers
            print("EEE")
            answer = input(prompt)
            num_tries += 1

        # output the correct answer if the user has exceeded the maximum number of tries
        if answer != str(x + y):
            print(str(x) + " + " + str(y) + " = " + str(x + y))

        # otherwise, increment the score for correct answers
        else:
            score += 1

        # increment the current problem number
        problem_num += 1

    # output the final score
    print("Score: " + str(score))


def get_level():
    # loop until the user enters a valid level
    while True:
        level = input("Enter a level (1, 2, or 3): ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    # raise an error for invalid levels
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level")

    # generate a random integer with the specified number of digits
    max_num = 10 ** level - 1
    return random.randint(0, max_num)


if __name__ == "__main__":
    main()