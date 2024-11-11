#Division Calculation
numerator = int(input("Enter the numerator:"))
denominator = int(input("ENter the denominator"))
try:
    result = numerator/denominator
    print("The result is:", result)
except ZeroDivisionError:
    print("Cannot devide by zero")
except ValueError:
    print("Enter valid integers")