total_bill = int(input("Enter your total bill: "))

is_member = bool(input("Are you a member? (yes or no) "))

discount = 0

final_amount = 0

    if total_bill >= 1000 and is_member == "yes":
        discount = total_bill * 0.1
        final_amount = total_bill - discount
        
    elif total_bill >= 1000 and is_member != "yes":
        discount = total_bill * 0.05
        final_amount = total_bill - discount
        
    else:
        discount = 0
        final_amount = total_bill

print("your discount is: ", discount, " and your bill is: ", final_amount)