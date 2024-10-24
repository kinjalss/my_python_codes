#bubble sort technique

def bubble_sort(a):
  for i in range(len(a)):
    for j in range(len(a)-i-1):
      if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
  return a
a=[]
n=int(input("enter the number of elements"))
for i in range(n):
  b=int(input(f"enter element {i+1} : "))
  a.append(b)
print("sorted list",bubble_sort(a))