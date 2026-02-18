char=input()
u=0

for i in char:
    n=ord(i)
    u+=n
avg=u/len(char)
print(f"{avg:.2f}")