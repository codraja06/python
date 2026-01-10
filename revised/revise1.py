# Login System
def login():
    user_db={
        'rajaram@123':'raja@123',
        'luffy@123':'strawhat@123',
        'naruto@123':'ramen@123'
    }
    
    email=input("Enter your email=")
    while email not in user_db:
        print("Email does not exist")
        email=input("Enter your email Again=")
    
    password=input("Enter your password=")
    while password != user_db[email]:
        print("password incorrect")
        password=input("Enter your password Again=")
    
    print("Successfully Logged in")


login()
    