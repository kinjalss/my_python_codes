import math

print("acos:", math.acos(0.55))  # Arc cosine of 0.55 (input must be in range [-1, 1])
print("acosh:", math.acosh(5))   # Inverse hyperbolic cosine of 5 (input must be >= 1)
print("asin:", math.asin(0.55))  # Arc sine of 0.55 (input must be in range [-1, 1])
print("asinh:", math.asinh(0.55))  # Inverse hyperbolic sine of 0.55 (no restrictions on input)
print("atan:", math.atan(0.55))  # Arc tangent of 0.55 (no restrictions on input)
print("atanh:", math.atanh(0.55))  # Inverse hyperbolic tangent of 0.55 (input must be in range (-1, 1))
print("ceil:", math.ceil(12.78))  # Smallest integer greater than or equal to 12.78
print("factorial:", math.factorial(6))  # Factorial of 6 (6!)
print("gcd:", math.gcd(3, 18))  # Greatest common divisor of 3 and 18
print("pow:", math.pow(4, 3))  # 4 raised to the power of 3
print("degrees:", math.degrees(-0.87))  # Converts radians (-0.87) to degrees
print("floor:", math.floor(7.8))  # Largest integer less than or equal to 7.8
print("sqrt:", math.sqrt(481))  # Square root of 481
print("copysign:", math.copysign(4, -1))  # Returns 4 with the sign of -1


#abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
n=int(input("enter n:"))
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")

#all leap year in 1900-2100
print("the leap years:\n ")
for i in range(1904,2097,4):
  print(i)


# 20 horizontal stars
for i in range(1,21):
  print("*")

#multiplication table
n=int(input("enter n :"))
for i in range(1,11):
  print(n,"x",i,"=",i*n)

#sum of first 10 natuarl numbe4rs
s=0
for i in range(1,11):
  s=s+i
  i=i+1
print(s,"sum of all natural numbers")
