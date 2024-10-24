# write a program to swap 2 variables with and without using a 3rd variable
a = 2
b = 5

#  without 3rd variable
a,b = b,a
print(a)
print(b)

#  using 3rd variable
c = a
a = b
b = c
print(a)
print(b)