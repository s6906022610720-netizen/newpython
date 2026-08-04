global_variable = "I'm outside the function"

def my_function():
    print(global_variable)  # Accessing the global variable inside the function

#
my_function() # Output: I'm a global variable

#
print(global_variable)  # Accessing the global variable outside the function