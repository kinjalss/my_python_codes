#multipy two variables
def m(x,y):
  p=x*y
  return p

m(3,4)

# greet
def greet (n):
  print(f"hello,{n}!")
greet("navroop")

#global and local scope
x=5
def o():
  y=3
  def i():
    z=x+y
    return z
  return i()
o()

#add total
t=0
def add(n):
  global t
  t=t+n
  return t

add(10)

#largest of 2 and largest of 3
def largest(a,b):
  if a>b:
    return a
  else:
    return b
largest(10,20)
def largest_3(a,b,c):
  return largest(a,largest(b,c))
largest_3(10,20,30)

#wap python funation to find prime numbers in range 1 to 100
def prime():
  for i in range(1,101):
    if i>1:
      for j in range(2,i):
        if i%j==0:
          break
      else:
        print(i)
prime()

#wap python funtion to check given number is prime or not
def check(n):
  if n>1:
    for i in range(2,n):
      if n%i==0:
        print("not prime")
        break
    else:
      print("prime")
check(10)
check(2)