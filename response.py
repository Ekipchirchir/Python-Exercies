from validator_collection import validators

def email_validator(email):
    if validators.email(email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address: ")
    if email_validator(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
