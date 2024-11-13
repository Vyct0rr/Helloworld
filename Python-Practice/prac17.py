weight = int(input('what is your weight?: '))
unit = input('L(bs) or k(kg)')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Your weight is {converted}")

else:
    converted = weight / 0.45
    print(f"Your weight is {converted}")