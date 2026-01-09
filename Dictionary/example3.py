user = {
    'rajaram@123': 'raja@123',
    'qwerty@123': 'qwerty@123',
    'uiop@123': 'uiop@123'
}

doc = input("Login or signup: ").lower()

if doc == "login":
    
    email = input("Enter the Email: ")
    password = input("Enter the Password: ")

    if email in user and user[email] == password:
        print("Login successful ✅")
    else:
        print("Invalid email or password ❌")

elif doc == "signup":
    
    email = input("Enter the new Email: ")
    password = input("Enter the new Password: ")

    if email in user:
        print("Email already exists ❌")
    else:
        user[email] = password
        print("User ID added successfully ✅")

else:
    print("Error ❌")
