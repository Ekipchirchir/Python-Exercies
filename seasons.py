import sys
from datetime import date


def age_in_minutes(date_of_birth):
    try:
        dob = date.fromisoformat(date_of_birth)
    except ValueError:
        sys.exit("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    age_in_seconds = (date.today() - dob).total_seconds()
    age_in_minutes = round(age_in_seconds / 60)
    return age_in_minutes


def main():
    date_of_birth = input("Enter your date of birth in YYYY-MM-DD format: ")
    age_in_minutes_str = str(age_in_minutes(date_of_birth))

    minutes = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
               "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    tens = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty"}

    if len(age_in_minutes_str) == 1:
        print(minutes[age_in_minutes_str] + " minute")
    elif len(age_in_minutes_str) == 2:
        if age_in_minutes_str[0] == "1":
            if age_in_minutes_str[1] == "0":
                print("ten minutes")
            elif age_in_minutes_str[1] == "1":
                print("eleven minutes")
            elif age_in_minutes_str[1] == "2":
                print("twelve minutes")
            else:
                print(minutes[age_in_minutes_str[1]] + "teen minutes")
        else:
            print(tens[age_in_minutes_str[0]] + minutes[age_in_minutes_str[1]] + " minutes")
    else:
        print("Sorry, this program only supports age calculation up to 99 minutes.")


if __name__ == "__main__":
    main()
