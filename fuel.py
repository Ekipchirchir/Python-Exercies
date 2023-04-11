# initialize input variables to non-integer values to enter the while loop
X = None
Y = None

# loop until valid input is entered
while True:
    # prompt the user for input
    fraction = input("Enter a fraction formatted as X/Y, where each of X and Y is an integer: ")
    
    # try to split the fraction into X and Y integers, catching any exceptions
    try:
        X, Y = map(int, fraction.split('/'))
    except ValueError:
        print("Invalid input, please enter a fraction formatted as X/Y, where each of X and Y is an integer.")
        continue
    except ZeroDivisionError:
        print("Invalid input, Y cannot be 0.")
        continue
    
    # check that X is less than or equal to Y, and that Y is not 0
    if X > Y or Y == 0:
        print("Invalid input, please enter a fraction where X is less than or equal to Y, and Y is not 0.")
        continue
    
    # break out of the loop if valid input is entered
    break

# calculate the fuel percentage
fuel_percentage = int(X / Y * 100 + 0.5)

# check if the tank is essentially empty or full
if fuel_percentage <= 1:
    fuel_status = "E"
elif fuel_percentage >= 99:
    fuel_status = "F"
else:
    fuel_status = str(fuel_percentage)

# output the fuel status
print("The tank is", fuel_status)