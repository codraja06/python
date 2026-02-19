vowel="aeiou"
word="hello"
c=[]
for i in word:
    if i in vowel:
        c+=i
print(len(c))
    