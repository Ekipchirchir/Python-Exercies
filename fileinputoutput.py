name = input("what is you name?")

file = open("names.txt", "w")
file.write(name)
print('Hello,  + {name}')
file.close 