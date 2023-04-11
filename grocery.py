from collections import Counter

# Prompt the user for items and store them in a list
items = []
while True:
    try:
        item = input().strip().lower()
        items.append(item)
    except EOFError:
        break

# Count the occurrences of each item and sort the items alphabetically
counts = Counter(items)
items = sorted(counts.keys())

# Output the grocery list with counts and in uppercase
for item in items:
    count = counts[item]
    print(f"{count:2d} {item.upper()}")