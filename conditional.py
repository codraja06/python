#1.Write a program to check if a number is positive, negative, or zero.
""""
n=int(input("Enter the number :"))

if n==0:
    print("Zero")
elif n>0:
    print("positive")
else:
    print("Negative")
    
    """
    
#2.Check if a given year is a leap year.
"""
n=int(input("Enter the year to find the leap year :"))

if n%4==0:
    print("leap year")
else:
    print("not a leap year")
    
"""

#3.Take three numbers and print the largest.
"""

print("to find largest number :")
a=int(input("Enter the number a :"))
b=int(input("Enter the number b :"))
c=int(input("Enter the number c :"))
d=max(a,b,c)
print(f"largest number {d}")

"""

#4.Write a simple grading system (marks input → grade output).
"""
maths=int(input("Enter the maths mark :"))
physics=int(input("Enter the physics mark :"))
chemistry=int(input("Enter the chemistry mark :"))
tamil=int(input("Enter the tamil mark :"))
english=int(input("Enter the english mark :"))
computer=int(input("Enter the computer mark :"))
per=maths+physics+chemistry+tamil+english+computer
perc=per/6

print(f"percentage :{perc:.2f}")

if perc > 90:
    print("A+ grade")
elif perc > 80:
    print("A grade")
elif perc >70:
    print("B+ grade")
elif perc >60:
    print("B grade")
elif perc >50:
    print("C grade")
else:
    print("U grade")
"""

#5.Check if a number is even or odd.
"""
n=int(input("Enter the number :"))
if n%2==1:
    print("odd")
else:
    print("even")
"""