weight = int(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

result = ""

if bmi < 18.5:
    result = "Underweight"
        
elif bmi >= 18.5 and bmi <= 24.9:
    result = "Normal"
        
elif bmi >= 55 and bmi <= 29.9:
    result = "Overweight"
        
else:
    result = "Obese"
         
print(result)