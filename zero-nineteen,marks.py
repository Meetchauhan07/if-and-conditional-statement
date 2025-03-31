#zeo to nineteen
def number():
    num=int(input("enter the number"))
    words= ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 0<num<=19:
        return words[num]
    else:
        return "Number out of range (0-19)"
print(number())
'''
output:
enter the number5
five
'''
#marks
m1=int(input("Enter marks 1:"))
m2 =int(input("Enter marks 2:"))
m3 =int(input("Enter marks 3:"))

total=m1+m2+m3
avg=total/3

if m1<=39 or m2<=39 or m3<=39:
    result="fail"
else:
    result="pass"


print("Total: ",total)
print("Average: ",avg)
print("Result: ",result)

def grade(mark):
    if mark >= 80:
        return "O"
    elif mark >= 70:
        return "A+"
    elif mark >= 60:
        return "A"
    elif mark >= 55:
        return "B+"
    elif mark >= 50:
        return "B"
    elif mark >= 45:
        return "C"
    elif mark >= 40:
        return "P"
    else:
        return "F"
print("Grades:")
print("Subject 1: ",grade(m1))
print("Subject 2: ",grade(m2))
print("Subject 3: ",grade(m3))
'''
output:
Enter marks 1:50
Enter marks 2:43
Enter marks 3:24
Total:  117
Average:  39.0
Result:  fail
Grades:
Subject 1:  B
Subject 2:  P
Subject 3:  F
'''











