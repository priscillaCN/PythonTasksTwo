password = len(input("enter your password: "))
password_strength = ""

if password < 6:
    password_strength = "weak"
    
elif password >= 6 and password <= 10:
    password_strength = "medium"
        
else:
    password_strength = "strong"
        
print(password_strength)        
    