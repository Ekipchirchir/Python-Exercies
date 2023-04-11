def main():
    greeting = input("Enter a greeting: ")
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
