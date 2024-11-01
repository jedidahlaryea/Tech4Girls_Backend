#!/usr/bin/python3
"""numbers = [1,5,3,8]
numbers.append(10)
numbers.insert(1, 2)
numbers.remove(3)
print(numbers)

"create a list called colour containing red green blue yellow purple,sort the list alphabetically"
"reverse the sorted listprint the final list"

colours = ['red','green','blue','yellow','purple']
print(colours.sort())
print(colours)
colours.sort(reverse=True)
print(colours)

"create a list called temperatures containing 25 18 32 20 28"
"find the minimum temp find the maximun temp print both values"

temperatures = [25,18,32,20,28]
print(min(temperatures))
print(max(temperatures))
print(temperatures)

"create a list called animals containing dog cat bird fish"
"remove the element at index 2"
"replace the element at index 1 with lizard use pop to remove and return the last element" 
"print the final list"

animals = ['cat','dog','bird','fish']
animals.remove('fish')
animals.remove('dog')
animals.insert(1,'lizard')
popped=animals.pop()
print(popped)
print(animals)

list1 =[]
"""
"""
students = {'name': 'harriet', 'age': 20, 'city': 'Accra'}
for key, value in students.items():
    print(f"{key}:{value}")

grades = [85, 72, 90, 68, 80]
for grade in grades:
    if grade > 80:
       print (grade)
average = sum(grades) / len(grades)
print("average grades",average)       
"""
products =[('Apple', 1.29), ('Banana', 0.59), ('Orange', 0.79)]
for string, integer in products:
    print(f"Products: {string} - Price: {integer}")                                                                                                                                                  