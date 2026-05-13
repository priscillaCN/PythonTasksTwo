multiple = int(input("Enter a number: "))
product = 0

for number in range(1, 11):
    product = multiple * number
    print(multiple, " X ", number, " = ", product)
    