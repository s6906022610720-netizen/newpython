try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator
    print(f"the reult is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Plese enter numeric values.")

finally:
    print("Execution completed,whether an exception occurred or not.")

print("End of program")