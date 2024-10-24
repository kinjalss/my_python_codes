#Distance Calculator of two points
x1 = float(input("X Coordinate of Point 1")) 
y1 = float(input("Y Coordinate of Point 1"))
x2 = float(input("X Coordinate of Point 2"))
y2 = float(input("Y Coordinate of Point 2"))

Distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
Distance = round(Distance , 2) 
print("Distance Between the Given Points are :" , Distance)

#To print the digit on one's place
x = float(input('Please Enter a number :'))
x = x % 10
print("digit on one's place is ",int(x) )