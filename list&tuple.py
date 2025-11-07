#1.create a list of 5 numbers and print their sum.
"""
num=[1,2,3,4,5]
print(sum(num))
"""
#2.Write a program to find the largest and smallest number in a list.
"""
num=[55,66,33,22,11,1]
print(f"maximum number in a list :{max(num)}")
print(f"minimum number in a list :{min(num)}")
"""
#3.Replace the second element of a list with a new value.
"""
num=[22,33,55,66,88]
num[1]=44
print(f"replace the 2nd element : {num}")
"""
#4.Convert a tuple into a list and modify it
"""
tuple=(33,44,55,66,88)
lst=list(tuple)
lst[1]=66
print(lst)
"""
#5.Take a 5 inputs from the user and stores them in a list
"""
lst=[]
for i in range(5):
    num=input("Enter the element : ")
    lst+=num
print(lst)
"""