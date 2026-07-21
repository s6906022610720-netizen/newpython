# This program calculates sales commissins.
# Create a variable to control the loop
keep_going = 'y'

# Calculate a seaies of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commision rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commision rate: '))

    # Calculate the commision.
    commision = sales * comm_rate

    # Display the commision.
    print(f'The commision is ${commision:.2f}')

    # See if the user wants to do another one.
    krrp_going = input('Do you want to calculate another' + \
                       ' commision (Enter y for yes): ')