from collections import Counter
n=input("Enter the string:")
f=Counter(n)
for key,value in f.items():
    print(f"{key}={value}")