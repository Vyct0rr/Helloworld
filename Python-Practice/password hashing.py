import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Function to verify a password against a hash
def verify_password(stored_hash, password_to_check):
    # Hash the input password
    hashed_input = hash_password(password_to_check)
    # Compare the hashed input with the stored hash
    return hashed_input == stored_hash

# Example Usage
# Input password (Example: user's password)
user_password = "SecurePassword123"

# Hashing the password
hashed_password = hash_password(user_password)
print(f"Original password: {user_password}")
print(f"Hashed password: {hashed_password}")

# Verifying the password
password_to_verify = "SecurePassword123"  # Correct password
is_verified = verify_password(hashed_password, password_to_verify)
print(f"Password verification (correct password): {is_verified}")

# Attempting to verify with an incorrect password
wrong_password = "WrongPassword"
is_verified_wrong = verify_password(hashed_password, wrong_password)
print(f"Password verification (incorrect password): {is_verified_wrong}")


