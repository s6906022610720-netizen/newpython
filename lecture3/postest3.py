work_hour = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly pay rate: "))

if work_hour > 40:
    pay = (work_hour - 40) * hourly_rate * 1.5 + 40 * hourly_rate
else:
    pay = work_hour * hourly_rate
print(f"The gross pay is ${pay:,.2f}.")