#Matt Westelman
#1/18/18
#slope.py - What is the slope?

xPoint1 = float(input("x1 = "))
yPoint1 = float(input("y1 = "))
xPoint2 =float(input("x2 = "))
yPoint2 = float(input("y2 = "))

print("slope = ", round((xPoint1-xPoint2)/(yPoint1 - yPoint2), 3))
slope = round((xPoint1-xPoint2)/(yPoint1 - yPoint2), 3)
b =  yPoint1-slope*xPoint1
print("b = ", b)
print ("y = ", slope, "x + ", b)  
