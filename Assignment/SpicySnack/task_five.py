year = int(input("Enter any year: "))

is_leapyear = False

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leapyear = True
    print(year, "is a leapyear")
        
else:
    print(year, "is not a leapyear")