def psc(password):
    digit=False
    special_char="!@#$%^&*())"
    special=False
    
    if len(password)<8:
        return "Weak Passwod"
    
    for char in password:
        if char.isdigit():
            digit=True
        if char in special_char:
            special =True
            
    if digit and special:
             return "Strong password "
    elif digit or special:
             return "Medium password "
    else:
        return "Weak password "
    
psd=input("Enter the password:")
print(psc(psd))