#1.leap year using function
def leap_year(year):
    if (year % 4==0 and year %100!=0) or (year % 400 ==0):
        print("It is a leap Year")
    else:
        print("It is not a leap Year")

year=int(input())

leap_year()