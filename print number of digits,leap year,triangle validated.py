#print number of digits
num=input("Enter a number:")
count = 0
for char in num:
    if char in '0123456789':  
        count += 1
    elif char == '-' and count==0:  
        continue
    else:
        print("Invalid number.")
print("Number of digits:",count)
'''
output:
Enter a number:-131
Number of digits: 3
'''
#leap year
year=int(input("Enter the year:"))
if (year%400==0) or (year%100 !=0 and year%4==0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")
'''
output:
Enter the year:2006
2006  is not a leap year
'''
#Triangle is valid or not
a=int(input("Enter the first angle"))
b=int(input("Enter the second angle"))
c=int(input("Enter the third angle"))
if (a+b+c==180):
    print("Triangle is valid")
else:
    print("Triangle is invalid")
'''
output:
Enter the first angle55
Enter the second angle60
Enter the third angle65
Triangle is valid
'''

    





