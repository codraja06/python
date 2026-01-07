#3.Find the sum of all even numbers from 1 to 100.

n=0
for i in range(1,101):
    if i%2==0:
        n+=i
print(n)