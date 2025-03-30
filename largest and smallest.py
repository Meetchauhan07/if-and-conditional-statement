#largest and smallest(2 numbers)
a=5
b=9
if a>b:
    print('largest number:',a)
    print('smallest number:',b)
else:
    print('smallest number:',a)
    print('largest number:',b)
'''
output:
smallest number: 5
largest number: 9
'''
#largest and smallest(3 numbers)
a=584
b=924
c=793
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print("Largest:",largest)

if a<=b and a<=c:
    smallest=a
elif b<=a and b<=c:
    smallest=b
else:
    smallest=c
print("smallest:",smallest)
'''
output:
Largest: 924
smallest: 584
'''
