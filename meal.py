def main():
    # Prompt user for time in 24-hour format
    time_str = input("Enter a time in 24-hour format (e.g. 7:30): ")

    # Call convert function to convert time_str to float hours
    time = convert(time_str)

    # Determine which meal, if any, corresponds to the input time
    if 7.0 <= time < 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time < 13.0:
        print("It's lunch time!")
    elif 18.0 <= time < 19.0:
        print("It's dinner time!")


def convert(time):
    # Split time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to floats and return their sum
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
