#Binary Search
#Binary Search always demand Sorting Of list / array
import math
list = [10,20,34,678,123,89,30,40,79,23,89,50]
list.sort()
print(list)
target = int(input("Pls Enter The Target Element You Want To Find in The List: "))
left = 0
right= len(list) - 1
while left<=right:
    mid = (left + right)//2
    if list[mid] == target:
        print(f"{target}found at index {mid}")
        break
    elif list[mid]<target:
        left = mid +1
    else:
        right = mid-1
else:
    print(f"{target} not found in the given list.")