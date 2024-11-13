# Mock data: Pre-stored usernames and passwords
users = {
    "Victor": "password123",
    "Alice": "alice2024",
    "John": "johnSecure!"
}


# Register a new user
def register():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    # Check if the user already exists
    if name in users:
        print("Username already exists. Please choose another name.\n")
    else:
        # Store the name and password in the dictionary
        users[name] = password
        print("Account created successfully!\n")


# Allow the user to log in
def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    # Check if the name exists and the password matches
    if name in users and users[name] == password:
        print(f"Login successful! Welcome, {name}\n")
    else:
        print("Invalid username or password. Please try again.\n")


# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':x
        login()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
