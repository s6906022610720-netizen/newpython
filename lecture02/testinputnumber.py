# get the user's name, age, and income.
name = input('What is your name?')
age = input('what is your age?')
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered:')
print('name:',name)
print('age:',age)
print('Income: ',format(income, '10,.2f'))