# Print the table headings.
print('KPH\MPH')
print('-------')

# print the KPH 1 through 3
# and their MPH.
for KPH in range(60,140,10):
    MPH = KPH*0.6214
    print(KPH, '\t', MPH)