def fahrenheit(celsius):

    return (9 / 5) * celsius + 32


print(f'{"Celsius":>10}{"Fahrenheit":>12}')

for celsius in range(101):

    print(f'{celsius:>10}{fahrenheit(celsius):>12.1f}')