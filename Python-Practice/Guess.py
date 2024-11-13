secret_number = 13

guess_number = int(input('guess the number: '))

while guess_number != secret_number:
    print('Wrong guess. Try again.')
    guess_number = int(input('guess the number: '))

else:
    print('YAY! You guessed the number correctly!')
