# prompt the user for input
string = input("Enter some text: ")

# define a set of vowels in both uppercase and lowercase
vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

# iterate over each character in the text
output = ''
for char in string:
    # if the character is not a vowel, add it to the output string
    if char not in vowels:
        output += char

# output the string with vowels removed
print(output)