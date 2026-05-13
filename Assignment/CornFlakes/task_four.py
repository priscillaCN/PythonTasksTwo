result = ""

for student in range(1, 16):
    
    score = int(input("Enter student score: "))
    if score >= 45:
        result = "pass"
    else:
        result = "fail"
        
    print(result)