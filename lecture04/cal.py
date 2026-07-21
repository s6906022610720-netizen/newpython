# This program calculates the sum of a series of number the user enter.

max = 5 # The maximum number
# Initializa an accumulator variable.
total = 0.0

# Explain what we are doing.
print('This program calculates the sum of')
print(max, 'numbers you will enter.')

# Get the numbers and accumulate them.
for couter in range (max):
    number = int(input('Enter a number: '))

# Display the total of the numbers.
print('The total is', total)