#Dictoionary Lookup
data = {"name":"Alice", "age":25, "country":"Wonderland"}
key = input("Enter the key youwant to look up: ")
try:
    print("Value:",data[key])
except KeyError:
    print(f"The key'{key}' does not exist in the dictionary")
    