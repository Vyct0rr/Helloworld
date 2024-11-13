users = {
   "Meseko Victor" : "Meseko",
    "John Kennedy" : "John",
     "Alice abel" : "abel"
}

def register():
  name = input("Enter your username: ")
  password = input("Enter your password: ")


  if name in users:
        print("Username already exists. Please choose another name.")

  if len(password) < 4:
       print("Password must be at least 4 characters!")
  else:
      users[name] = password
      print("Account created successfully!")

def login():
 name = input("What is your username")
 password = input("What is your password")

 if name in users and users[name] == password:
     print("Login successful!")

 else:
        print("Invalid username or password. Please try again.")

while True:
    print ("\n1. Register")
    print("2. Login")
    print("3. Exit the program")
    choice = input("\n Please select an option: ")

    if choice == '1':
        register()

    elif choice == '2':
        login()

    elif choice == '3':
        print ('Existing the program!')
        break
    else:
        print('Invalid choice')

