#List Index Access
items =["apple", "banana", "cherry"]
index = int(input("Enter the index of the number you want to access"))
try:
    print("You selected:",items[index])
except IndentationError:
    print(f"Index'{index}'cannot be found on the list")
