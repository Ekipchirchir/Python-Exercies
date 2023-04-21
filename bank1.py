def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Enter greeting: ")
    print(value(greeting))


if __name__ == "__main__":
    main()
