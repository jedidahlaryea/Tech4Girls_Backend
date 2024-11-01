#Control Flow
#Syntax
"""
if condition:
    statement
elif condition
    statement
elif condition 
    statement
else
    statement            
"""
"""my_string = 'Hello flow control'

if my_string == 'Hello control flow':
    print(True)
elif my_string == 'Hello flow control':
    print('good')    
else:
    print(False)    
"""
"""my_set = {1, 2, 3, 4}
if 9 and 2 in my_set:
    print('Inclusive')
else:
    print('Exclusive')
"""
"""number = 7
if number == (number%2 == 0):
    print('Even')
else:
    print('Odd') 
"""
"""#For loops in python
items = [2, 4, 6, 8, 10, 12]
#Syntax
for item in items:
    print(item)
if item == 8:
    print('Skipped 8')
print(item)

for item in range(1,11):
    print(item)
"""    
"""items = [2, 4, 6, 8, 10, 12] 
for item in items:#outer loop
    for letter in 'abcdefg': #inner loop
        print(item, letter)

things = (2, 4, 6, 8, 10, 12)
for thing in things:
     print(thing)     
"""     

#for loops in  python
my_dict = {'name': 'Jedidah', 'age': 19, 'work': 'T4G Scholar', 'energy_level': 80}
for key, value in my_dict.items():
    print(key, value)

for key in my_dict.keys():
    print(key)    
for value in my_dict.values():
    print(value)    


#first loop through a range of numbers from 1-50
for i in range(1, 51): 

#if number is/ 3 and returns 0 print Fizz
    if (i % 3 == 0):
#number is divisible by both 3 and 5 ,print Fizzbuzz
    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
