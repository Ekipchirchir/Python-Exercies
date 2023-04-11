names = []

# Read names from user input
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break

# Bid adieu to the names
count = len(names)
if count == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif count == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif count > 2:
    last_name = names[-1]
    names_except_last = names[:-1]
    names_except_last_str = ", ".join(names_except_last)
    print(f"Adieu, adieu, to {names_except_last_str}, and {last_name}")
