#2.Print the multiplication table of a number given by the user.

num=int(input("Enter the number for multiplication table :"))
for i in range(1,11):
    print(f"{i} x {num} = {i*num}")