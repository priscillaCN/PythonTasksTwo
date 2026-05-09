father_age = int(input("Enter father's age between 1 & 80: "))

son_age = int(input("Enter son's age between 1 & 80: "))

year = father_age - (2 * son_age)

if year > 0:
    print(f"father was twice his son's age {year} year(s) ago.")
        
elif year < 0:
    print(f"father will be twice his son's age in {year} year(s).")
        
else:
    print(f"father is currently twice his son's age.")
        
    
        
    
        