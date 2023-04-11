# prompt user for camel case variable name
camel_case_var = input("Enter a variable name in camel case: ")

# initialize an empty string for the snake case variable name
snake_case_var = ""

# loop through each character in the camel case variable name
for i in range(len(camel_case_var)):
    
    # if the character is uppercase and not the first character
    if camel_case_var[i].isupper() and i != 0:
        
        # add an underscore followed by the lowercase version of the character to the snake case variable name
        snake_case_var += "_" + camel_case_var[i].lower()
    
    # otherwise, add the lowercase version of the character to the snake case variable name
    else:
        snake_case_var += camel_case_var[i].lower()

# output the converted snake case variable name
print("The snake case version of", camel_case_var, "is", snake_case_var)