age = int(input("Enter any age: "))

ticket_price = ""

	if age < 5:
        ticket_price = "free"
        
    elif age >= 5 and age <= 12:
        ticket_price = "$5"
        
    elif age >= 13 and age <= 64:
        ticket_price = "$12"
        
    else:
        ticket_price = "$8"
        
print("ticket price is: ", ticket_price)