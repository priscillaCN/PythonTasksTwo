number1 = int(input("Enter first number: "))

number2 = int(input("Enter second number: "))

operator = input("select your operator (+,-,*,/)")

result = 0

    if operator == "+":
        result = number1 + number2
        
    elif operator == "-":
        result = number1 - number2
        
    elif operator == "*":
        result = number1 * number2
        
    else:
        result = number1 / number2
        
print(result)
        