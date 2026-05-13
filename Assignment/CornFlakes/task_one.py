sum = 0

for number in range(1, 20_001):
    
	if number % 10 == 0:
		sum += number
    
print(sum)