#1.Print numbers from 1 to 10 using a for loop.
"""
for i in range(1,11):
    print(i,end=" ")
"""

#2.Print the multiplication table of a number given by the user.
"""
num=int(input("Enter the number for multiplication table :"))
for i in range(1,11):
    print(f"{i} x {num} = {i*num}")
"""

#3.Find the sum of all even numbers from 1 to 100.
"""
n=0
for i in range(1,101):
    if i%2==0:
        n+=i
print(n)
"""

#4.Reverse a number using a while loop.
"""
n=int(input("Enter the number to reverse :"))
rev=0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)
"""
#5.Print all numbers divisible by 3 and 5 between 1 and 100.
"""
for i in range(1,101):
    if i % 3==0 and i%5==0:
        
        print(i,end=" ")
"""