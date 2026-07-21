# Program to find the sum of all number stored in a list
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# Variable to store the sum
sum = 0

# Iterate over the list
for val in numbers:
    sum += val
    print(sum)

print("The sum is", sum)
