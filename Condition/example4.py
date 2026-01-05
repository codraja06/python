#4.Write a simple grading system (marks input → grade output).

maths=int(input("Enter the maths mark :"))
physics=int(input("Enter the physics mark :"))
chemistry=int(input("Enter the chemistry mark :"))
tamil=int(input("Enter the tamil mark :"))
english=int(input("Enter the english mark :"))
computer=int(input("Enter the computer mark :"))
per=maths+physics+chemistry+tamil+english+computer
perc=per/6

print(f"percentage :{perc:.2f}")

if perc > 90:
    print("A+ grade")
elif perc > 80:
    print("A grade")
elif perc >70:
    print("B+ grade")
elif perc >60:
    print("B grade")
elif perc >50:
    print("C grade")
else:
    print("U grade")