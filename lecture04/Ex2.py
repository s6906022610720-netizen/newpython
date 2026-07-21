# This program calculates sales commissins.
# Create a variable to control the loop
keep_going = 'y'

# Calculate a seaies of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commision rate.
    sales = float(input('Enter the amount of wholesale cost: '))
    comm_rate = float(input('Enter the commision retail price: '))

    # Calculate the retail price.
    retail price = wholesale cost*2.5

    # Display the commision.
    print(f'The commision is ${commision:.2f}')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another' + \
                       ' commision (Enter y for yes): ')