def main():
    expression = input("Enter an arithmetic expression in the format 'x y z', with one space between x and y and one space between y and z: ")
    x, operator, z = expression.split()

    # Convert the operands to float values
    x = float(x)
    z = float(z)

    # Perform the arithmetic operation based on the operator
    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z

    # Output the result as a float with one decimal place
    print(f"Result: {result:.1f}")

if __name__ == '__main__':
    main()
