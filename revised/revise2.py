# Count Frequency of Words

sent="python is easy and python is powerful"
word=sent.split()
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
        
print(frequency)