x = int(input("Enter value for integer x: "))

y = int(input("Enter value for integer y: "))

result = ""

    if x > 0 and y > 0:
        result = "Q1"
        
    elif x < 0 and y > 0:
        result = "Q2"
        
    elif x < 0 and y < 0:
        result = "Q3"
        
    elif x > 0 and y < 0:
        result = "Q4"
        
    elif x == 0 and y == 0:
        result = "Origin"
        
    elif x != 0 and y == 0:
        result = "X-axis"
        
    else:
        result = "Y-axis"
        
print(result)