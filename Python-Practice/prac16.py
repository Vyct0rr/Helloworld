#using the len function to check the length of user name

user_name = input('what is your name: ')

if len(user_name) < 3:
    print('name must be at least 3 characters')

elif len(user_name) > 50:
    print('name can be a maximum of 50 characters')

else:
    print('name looks good!')