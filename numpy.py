import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
n1=a1.reshape(4,3)
print(n1)

n2=a1.reshape(2,3,2)
print(n2)

n3=a1.reshape(2,2,-1)
print(n3)

t=np.array([1,2,3,4])
for x in t:
  print(x)

t1=np.array([[1,2,3,4],[5,6,7,8]])
for x in t1:
  print(x)

t1=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in t1:
  print(x)

for x in t1:
  for y in x:
    for z in y:
      print(z)

t2=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(t2==4)
print(x)
y=np.where(t2%2==0)
print(y)
z=np.where(t2%2!=0)
print(z)

h=np.searchsorted(t2,7)
print(h)
h1=np.searchsorted(t2,6,side='right')
print(h1)

a=np.array([10,20,30,40,50,60])
a2=np.array([3,4,5,8,10,6])
ad=np.add(a,a2)
print(ad)
s=np.subtract(a,a2)
print(s)
m=np.multiply(a,a2)
print(m)
d=np.divide(a,a2)
print(d)
p=np.power(a,a2)
print(p)
d1=np.dot(a,a2)
print(d1)