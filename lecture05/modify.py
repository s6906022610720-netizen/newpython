counter = 0

def increment():
    global counter
    counter += 1

# Calling the function
increment()
increment()

# Accessing the modified global variable
print(counter)  # Output: 2