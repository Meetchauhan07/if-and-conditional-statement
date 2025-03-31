#straight line
x1=5
x2=6
x3=7
y1=5
y2=6
y3=7
a=((y2-y1)*(x3-x2))-((y3-y2)*(x2 - x1))
if a==0:
    print("The three points are collinear")
else:
    print("The three points are not collinear.")
'''
output:
The three points are collinear
'''
#point lies inside the circle or not
h,k=0,0
r=5
x,y=5,0
distance_sqr=((x-h)**2)+((y-k)**2)
if distance_sqr<r**2:
    print("The point lies inside the circle.")
elif distance_sqr==r**2:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
'''
output:
The point lies on the circle.
'''
