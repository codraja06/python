user={
    'rajaram@123':'raja@123',
    'qwerty@123':'qwerty@123',
    'uiop@123':'uiop@123'
}
print(user)

email=input("Enter the Email:")
password=input("Enter the Password:")

if email and password in user:
    print(True)
else:
    
    print(False)


"""
if email in user:
    print("Password:",user[email])
else:
    print("NOT FOUND")
"""