#list comprehension
#Syntax:
#New List = [expression for item in iterable if condition == True]

#write a program to print numbers from 1 to 100 by using list comprehension
n : [num for num in range (1 , 101)] # type: ignore
print(n)
#write a program to print even numbers from 1 to 100 by using list comprehension
n = [num for num in range (1 ,101) if num%2 == 0]
print(n)
#write a program to print numbers divisible by 7 from 1 to 100 by using list comprehension
n = [num for num in range (1 ,101) if num%7 == 0]
print(n)
#write a program to create a list of squares of even numbers from 1 to 10 using list comprehension
squares = [x**2 for x in range (1,11) if x%2 == 0]
print(squares)
#write a program to print a numbers 100 to 1 by using list comprehension
numbers = [num for num in range (100 , 0 , -1)]
print(numbers)
#write a program to print sequence of vowels from a given sentence by using list comprehension
sentence = "The Rocket came back from mars."
vowels = [char for char in sentence if char in "aeiou"]
print(vowels)
#write a program to print consonent from a given sentence by using list comprehension
sentence = "The Rocket came back from mars."
consonent = [char for char in sentence if char not in "aeiou"]
print(consonent)
#write a program to print vowels from a given sentence remove duplicates from output by using list comprehension
sentence = "The Rocket came back from mars."
vowels = {char for char in sentence if char in "aeiou"}
print(vowels)
#write a program to convert negative prices to zero from given list by using list comprehension
original_prices = [1.25, -9.45, 10.22, 3.7, -5.92, 1.16]
p = [prices if prices>0 else 0 for prices in original_prices]
print(p)