"""
name = input("What is your name?: ")
age = int(input("What is your age?: "))
amount =float(input("How much are you withdrawing"))
age = age +1

print(f'Your name, {name} and age {age} has been recorded  you are withdrawing, {amount}')
prompt = "Hello! Welcome to the Rock, Paper, Scissors, game, I would like to get more information about you"
prompt += "\nWhat is your name ?"
name = input(prompt)
print(f'Welcome {name} to the game. you can start now')
"""

#determine if a user can go to the university based on thier age if the 
# user is 18 or older ,print you are old enough to be enrolled
#else print you can enroll when you are a little older
"""
age = int(input("hello, how old are you"))
if age >= 18:
   print("\nYou are old enough to be enrolled")
else:
   print("\nYou will be able to enroll when you are a little older")

message = input("What kind of rental car would you like?: ")   
print(f'Let me see if i can find you a {message}')
"""

"""answer = int(input("How many people are in your dinner group?: "))
if answer >= 8:
    print("\nYou would have to wait for a table")
else:
    print("\nYour table is ready")   """ 
#While loop

current_number = 0
"""while current_number <= 10:
    if current_number == 5:
       print('Skipping 5')
       current_number += 1
       continue
    else:
       print(current_number)
       current_number += 1"""

"""while True:
    print(current_number)
    current_number += 1
    """

prompt = "Tell me something and i would repeat it to you\n It can be your name or anything you prefer\n Type quit when you are done:  "
"""while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(f'Your message was{message}')"""
#OR    
"""message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'your message was: {message}')"""

prompt = "Please enter some pizza toppings you prefer\n Type quit when yoy are done: "
while True:
    message = input(prompt)
    if message == 'quit':       
        break
    print(f'The {message} topping will be added to your pizza')