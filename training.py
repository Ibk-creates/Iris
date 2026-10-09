shape= input('Enter Shape: ')
shape = shape.lower()
if shape == 'circle':
    r=float(input('Enter radius (m): '))
    area= 3.142*r**2
    print('Area is ', area)
elif shape == 'rectangle':
    l=float(input('Enter Length (m): '))
    b=float(input('Enter Breadth (m): '))
    area= l*b
    print('Area is ', area)
elif shape == 'triangle':
    b=float(input('Enter Base (m): '))
    h=float(input('Enter Height (m): '))
    area= 0.5*b*h
    print('Area is ', area)
else:
    print('Invalid Shape')



temperature= float(input("Enter the temperature: "))
unit = input('Is the temperature in Celsius or Fahrenheit? (C/F): ')
if unit.lower() == 'c':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F")
elif unit.lower() == 'f':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")



addition= 10 + 3
subtraction= 10 - 3
multiplication= 10 * 3
division= 10 / 3
floor_division= 10 // 3
modulus= 10 % 3
exponentiation= 2 ** 5
print(addition, subtraction, multiplication, division, floor_division, modulus, exponentiation)


