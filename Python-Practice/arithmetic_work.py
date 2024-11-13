input_1 = float(input("Enter the first number here: "))

asking_operation  = input('input operation here: ')

input_2 = float(input("Enter the second number here: "))


operation = ['+', '-', '/', '*']

Addition = input_1 + input_2
Subtraction = input_1 - input_2
Multiplication = input_1 * input_2
division = input_1 / input_2

if asking_operation in operation:
  print(f'{Addition}')

elif asking_operation in operation:
  print(f'Multiplication {Subtraction}')

elif asking_operation in operation:
 print(f'Subtraction {Subtraction}')

elif asking_operation in operation:
  print(f'Division {division}')

else:
  print('Invalid operation!')
