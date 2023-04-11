import math

# Prompt user for mass in kilograms
mass = int(input("Enter the mass in kilograms: "))

# Calculate the energy equivalent using E=mc^2
c = 300000000  # speed of light in meters per second
energy = math.floor(mass * c**2)

# Output the equivalent number of Joules
print(f"The energy equivalent of {mass} kg of mass is {energy} J.")
