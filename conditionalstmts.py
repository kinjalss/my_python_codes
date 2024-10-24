# check which number is greatest in the three
a = int(input("Input First Number: "))
b = int(input("Input Second Number: "))
c = int(input("Input Third Number: "))

if a > b and a > c:
    print(f"The greatest number is: {a}")
elif b > a and b > c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")

# write a program to find leap year
year = int(input("Enter Any Year"))

if((year % 4) == 0):
  print("Year is a Leap Year")
else:
  print("Year is Not a Leap Year")

#program to determine whether a person is eligble to vote or not, if he is not eligible display how many yrs are there to be eligble 
age = int(input("Enter Your Age"))

if(age > 18):
  print("You are Eligible to Vote")
else:
  a = 18 - age
  print("You are not Eligible to Vote")
  print(f"You will be Eligible after {a} years")

#program which prompts the user to enter a number between 1 to 7 and display the corresponding day of the week

num = int(input("Enter A Number Between 1 and 7"))

if (num == 1):
  print("Monday")
elif (num == 2):
  print("Tuesday")
elif (num == 3):
  print("Wednesday")
elif (num == 4):
  print("Thursday")
elif (num == 5):
  print("Friday")
elif (num == 6):
  print("Saturday")
elif (num == 7):
  print("Sunday")
else:
  print("Invalid Input")


#program which prompts the user to enter a number between 1 to 7 and display the corresponding day of the week

num = int(input("Enter A Number Between 1 and 7"))
a = {1 : "Monday" ,2 : "Tuesday" ,3 : "Wednesday" ,4 : "Thursday" ,5 : "Friday" ,6 : "Saturday" ,7 : "Sunday"  }
if (num > 0 and num < 8):
    print(a[num])
else:
    print("Invalid Input")