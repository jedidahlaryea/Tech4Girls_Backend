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
"""
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
"""
"""
#SETS
my_students = {'Grace', 'Naomi','Emefa', 'Priscilla', 'Jenifer'}
my_other_students = {'Grace', 'Beatrice', 'Naomi', 'Rhoda', 'Manuella', 'Emefa'}
students = {'Jedidah', 'Talatu', 'Happy', 'Ameera'}
print(my_students.intersection(my_other_students))
print(my_students.difference(my_other_students))
print(my_students.union(my_other_students))
print(my_other_students.difference(my_students))
#OR
print(my_students.difference(my_other_students))
print(my_other_students & my_students)
print(my_other_students | my_students)
print(my_other_students - my_students)
numbers = [1, 5, 3, 8, 8, 5]
unique_numbers = set(numbers)
new_list = list(unique_numbers)
new_list.sort()
print(new_list) 

#how to create empty lists, tuples and sets
var = list(var)
var = set(var)
var = tuple(var)

var = []
var = ()
"""
"""
list3 = [1, 4, 3, 7, 5, 4]
newlist = set(list3)
print(newlist)
final_list = tuple(newlist)
print(final_list)
"""
"""#To add
my_set = {'James', 'Rhoda', 'Irene', 'Jedidah','Khadijah'}
my_set.add('Nana Afua')
print(my_set)
#To remove
my_set.remove('James')
print(my_set)
#OR my_set.discard(item)
my_set.pop()
print(my_set)
#to remove all items
my_set.clear()
print(my_set)
#to check for methods of a particular data type
print(help(str.find))
"""
#Dictionaries
"""
my_student = {'name':'Rhoda', 'age':'21', 'program':'Tech4girls'}
print(my_student['name'])
print(my_student['age']) 
print(my_student['program'])
#print(my_student['class', 'Not found'])
print(my_student.get('class'))
my_student['coursemate'] = 'Naomi'
print(my_student.get('coursemate'))
my_student['name'] = 'Jedidah'
print(my_student.get('coursemate'))
print(my_student)
print(my_student.keys())
print(my_student)
print(my_student.values())
print(my_student)

del my_student['program']
print(my_student)
my_student.pop('coursemate')
print(my_student)
my_student.update({'name':'Naomi', 'age':22, 'program':'HACSA', 'coursemate':'Akorfa'})
print(my_student)"""