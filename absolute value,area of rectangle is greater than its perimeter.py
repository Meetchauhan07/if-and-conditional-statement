#absolute value
num=float(input("Enter a number: "))
if num<=0:
    num=-num
print("Absolute value:",num)
'''
output:
Enter a number: -221
Absolute value: 221.0
'''

#area of the rectangle is greater than its perimeter
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
if (2*(l+b))<(l*b):
    print("Area of the rectangle is greater than its perimeter")
else:
    print("Area of the rectangle is not greater than its perimeter")
'''
output:
Enter the length50
Enter the breadth72
Area of the rectangle is greater than its perimeter
'''
