#1 . Write a program to take a user’s name and age, then print: "Hello <name>, you are <age> years old."
"""
name=str(input("Enter the name :"))
age=int(input("Enter the age :"))
print(f"Hello {name},you are {age} years old")

       output
       Enter the name :G Rajaram
       Enter the age :19
       Hello G Rajaram,you are 19 years old
"""

  
#2 . Find the sum, difference, product, and division of two numbers given by the user.
"""
num1=int(input("Enter the number A :"))
symbol=input("select the operator (+/-/*//) :")
num2=int(input("Enter the number B :"))
if symbol=="+" :
    print(num1+num2)
elif symbol=="-":
    print(num1-num2)
elif symbol=="*":
    print(num1*num2)
elif symbol=="/":
    print(num1/num2)
else:
    print("ERROR")
    
     output
    Enter the number A :23
    select the operator (+/-/*//) :+
    Enter the number B :12
    35
"""

#3.Swap two variables without using a third variable.
"""
a=int(input("number A:"))
b=int(input("number B:"))
a,b=b,a
print(f"number a {a}, number b {b}")

output
number A:23
number B:34
number a 34, number b 23

"""


#4.Write a program to calculate the area of a rectangle using user inputs.
"""

l=int(input("Enter the length :"))
b=int(input("Enter the breadth :"))
formula=l*b
print(f"The area of the rectangle : {formula}")

output
Enter the length :22
Enter the breadth :45
The area of the rectangle : 990

"""

#5.Check the type of each variable: a = 5, b = 2.5, c = "Python", d = True.
"""
a=5
b=2.5
c="Python"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

output
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

"""