#5.Print all numbers divisible by 3 and 5 between 1 and 100.

for i in range(1,101):
    if i % 3==0 and i%5==0:
        
        print(i,end=" ")