# len()
# lower()
# replace(target word,replaced word)
'''
message = "Hello, World"
print(len(message))
print(message[:-5])

print(message.lower())
print(message.upper())
print(count('o'))
print(message.replace('World', 'Universe'))
e_2 = "This is Naomi's class. Kofi said this, "happy"
'''
'''
name ='Naomi'
greeting = 'Welcome'
more_greeting = 'to the Backend Class'
#entire_greeting ="{} {} {}".format(name, greeting, more_greeting)
entire_greeting = f'{name} {greeting} {more_greeting}'

print(entire_greeting)
'''

my_string ='Hello, T4girls Backend'
print(my_string.upper())
print(my_string.lower())
print(my_string.count('e'))
print(my_string.find('Backend'))
print(my_string.replace('Backend', 'Frontend'))
name = 'Hi! I am Priscilla.'
motivate = 'I am so excited and motivated to learn more Python,'
program = 'thanks to the HACSA foundation'

entire_string = f'{name} {motivate} {program}'

print(entire_string)