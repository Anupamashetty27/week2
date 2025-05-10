import hashlib

# Dictionary to store username and hashed passwords
# In a real application, this would be stored in a database.
user_credentials = {}

def hash_password(password):
    """Hashes a password using SHA-256."""
    # Passwords need to be encoded to bytes before hashing
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the password bytes
    sha256.update(password_bytes)
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

def register(username, password):
    """Registers a new user by storing their username and hashed password."""
    if not username or not password:
        print("Error: Username and password cannot be empty.")
        return False
    if not isinstance(username, str) or not isinstance(password, str):
        print("Error: Username and password must be strings.")
        return False

    if username in user_credentials:
        print(f"Error: User '{username}' already exists. Please choose a different username.")
        return False
    else:
        hashed_pwd = hash_password(password)
        user_credentials[username] = hashed_pwd
        print(f"User '{username}' created successfully.") # Modified to match example style
        return True

def login(username, password):
    """Logs in a user by checking their username and hashed password."""
    if not username or not password:
        print("Error: Username and password cannot be empty for login.")
        return False
    if not isinstance(username, str) or not isinstance(password, str):
        print("Error: Username and password must be strings.")
        return False

    if username not in user_credentials:
        print(f"Login Failed: User '{username}' not found.")
        return False
    else:
        # Hash the provided password for comparison
        hashed_pwd_attempt = hash_password(password)
        # Compare with the stored hashed password
        if user_credentials[username] == hashed_pwd_attempt:
            print("Login Successful")
            return True
        else:
            print("Login Failed: Invalid password.")
            return False

# --- Example Usage as per the Task ---
if __name__ == "__main__":
    print("--- User Registration and Login System ---")

    # Registration examples
    print("\n--- Registration ---")
    register("john", "mypassword")    # Expected: User 'john' created successfully.
    register("jane", "securepass123") # Expected: User 'jane' created successfully.
    register("john", "anotherpass")   # Expected