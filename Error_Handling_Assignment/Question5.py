#Age validator 
try:
    age = int(input("Enter your age"))
    if age<0:
        print("Age cannot be negative!")
    elif age>120:
        print ("The age is !")
    else:
        print("Your age is:", age)
except ValueError:
    print("Please enter a valid integer for your age")   