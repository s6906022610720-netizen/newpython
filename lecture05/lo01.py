def my_function():
    local_variable = " I'm inside the function"
    print(local_variable)

# Call Function
my_function()

# Accessing local_variable from outside , an error
# print(local_variable)  # NameError : name 'local_variable' is not defined