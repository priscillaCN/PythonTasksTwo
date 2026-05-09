score1 = int(input("Enter first score: "))

score2 = int(input("Enter second score: "))

score3 = int(input("Enter third score: "))

average = (score1 + score2 + score3) / 3)

grade = ""

    if average >= 90 and average <= 100:
        grade = "A"
    
    elif average >= 80 and average <90:
        grade = "B"
        
    elif average >= 70 and average <80:
        grade = "C"

    elif average >= 60 and average <70:
        grade = "D"

    else:
        grade = "F"
        
print("Grade: ", grade)