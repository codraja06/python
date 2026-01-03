  
#2 . Find the sum, difference, product, and division of two numbers given by the user.

num1=int(input("Enter the number A :"))
symbol=input("select the operator (+/-/*//) :")
num2=int(input("Enter the number B :"))
if symbol=="+" :
    print(num1+num2)
elif symbol=="-":
    print(num1-num2)
elif symbol=="*":
    print(num1*num2)
elif symbol=="/":
    print(num1/num2)
else:
    print("ERROR")
    
