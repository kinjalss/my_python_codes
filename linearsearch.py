#linear Search
list = [10,20,30,40,50]
target = int(input("Pls Enter The Target Element You Want To Find in The List: "))
target = 10
found = False
for i in range (len(list)):
    if target == list[i]:
       print(f"{target} found at index", i)
       found = True
       break
else:
    print(f"{target} not found in the given list.")