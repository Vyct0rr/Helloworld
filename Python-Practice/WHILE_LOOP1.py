name= input('Enter your username ')
password = input('Enter your password ')

if len(password) < 6:
    print(f'Password should be at least 6 characters long')

else:
    print(f'Password is valid')