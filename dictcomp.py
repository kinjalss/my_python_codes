#Dict comprehension
#Syntax:
#New Dict = {key_expression : value expression for item in iterable if condition}

#write a program to print Squares of Dict from 1 to 5 using Dict comprehension
y = {num : num**2 for num in range (1,6)}
print(y)

#write a program to create a dict by using key list and value list by using Dict comprehension
MyDict = {keys[i] :  values[i] for i  in range (len(keys))} # type: ignore
keys = ['a','b','c','d']
values = [1,2,3,4]
print(MyDict)

#write a program to create a dict of square root of numbers from 100 to 1 by using Dict comprehension
import math 
sqrt = {x: math.sqrt(x) for x in range(100,95,-1)}
print(sqrt)

#write a program to print the names of python developer from given dict by using Dict comprehension
developers = {'Jane' : 'python' , 'Jade' : 'javascript' , 'jhon' : 'python' , 'doe' : 'ruby'}
y = {key : developers[key] for key in developers if developers[key] == 'python'}
print(y)

#write a program to create a dict of operating system with admin role and print only Ubuntu admins
admins = {'Jane' : 'mac' , 'Jade' : 'ubuntu' , 'jhon' : 'windows' , 'doe' : 'ubuntu'}
y = {key : admins[key] for key in admins if admins[key] == 'ubuntu'}
print(y)