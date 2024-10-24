def f(a):
  if a<4:
    b=a/(a-3)
    print("value of b is ",b)

try:
  f(3)
  f(5)
except ZeroDivisionError :
  print("zerodivision error occuredd and handled")

def aby(a,b):
  try:
    c=(a+b)/(a-b)
  except ZeroDivisionError:
    print("a/b result in  0")
  else:
    print(c)
aby(2.0,3.0)
aby(3.0,3.0)


try:
  k=5//10
  print(k)
except ZeroDivisionError:
  print("can't divide by zero")
finally :
  print("finally executed")
