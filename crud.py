# Initial list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# --- ID Generation ---
# Initialize next_id based on the current maximum ID in the list,
# or start from 1 if the list is empty.
# This ensures IDs are unique even if items are deleted.
if users:
    next_id = max(user["id"] for user in users) + 1
else:
    next_id = 1

def generate_id():
    """Generates a new unique ID."""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

# --- CRUD Functions ---

# CREATE: Add a new user
def add_user(name, email):
    """Adds a new user to the list."""
    if not name or not email:
        print("Error: Name and email cannot be empty.")
        return None
    if not isinstance(name, str) or not isinstance(email, str):
        print("Error: Name and email must be strings.")
        return None
    # Basic email format check (can be more sophisticated)
    if "@" not in email or "." not in email.split('@')[-1]:
        print("Error: Invalid email format.")
        return None

    new_user = {
        "id": generate_id(),
        "name": name,
        "email": email
    }
    users.append(new_user)
    print(f"User '{name}' added successfully with ID {new_user['id']}.")
    return new_user

# READ: Retrieve user data by ID
def get_user_by_id(user_id):
    """Retrieves a user by their ID."""
    if not isinstance(user_id, int):
        print("Error: User ID must be an integer.")
        return None
    for user in users:
        if user["id"] == user_id:
            return user
    print(f"User with ID {user_id} not found.")
    return None

# UPDATE: Update user data by ID
def update_user_by_id(user_id, new_name=None, new_email=None):
    """Updates an existing user's name and/or email by their ID."""
    if not isinstance(user_id, int):
        print("Error: User ID must be an integer.")
        return None

    user_to_update = None
    for user in users:
        if user["id"] == user_id:
            user_to_update = user
            break

    if user_to_update:
        updated_fields = []
        if new_name is not None:
            if not isinstance(new_name, str) or not new_name.strip():
                print("Error: New name must be a non-empty string.")
            else:
                user_to_update["name"] = new_name
                updated_fields.append("name")
        if new_email is not None:
            if not isinstance(new_email, str) or "@" not in new_email or "." not in new_email.split('@')[-1]:
                print("Error: New email must be a non-empty string with valid format.")
            else:
                user_to_update["email"] = new_email
                updated_fields.append("email")

        if updated_fields:
            print(f"User ID {user_id} updated ({', '.join(updated_fields)}).")
            return user_to_update
        else:
            print(f"No updates provided for User ID {user_id}.")
            return user_to_update # Return user even if no change, or None if preferred
    else:
        print(f"User with ID {user_id} not found for update.")
        return None

# DELETE: Delete user data by ID
def delete_user_by_id(user_id):
    """Deletes a user by their ID."""
    if not isinstance(user_id, int):
        print("Error: User ID must be an integer.")
        return False

    user_to_delete = None
    for user in users:
        if user["id"] == user_id:
            user_to_delete = user
            break

    if user_to_delete:
        users.remove(user_to_delete)
        print(f"User with ID {user_id} ('{user_to_delete['name']}') deleted successfully.")
        return True
    else:
        print(f"User with ID {user_id} not found for deletion.")
        return False

# --- Main Program / Example Usage ---
if __name__ == "__main__":
    print("--- Initial User List ---")
    for u in users:
        print(u)
    print("-" * 30)

    # CREATE examples
    print("\n--- Adding Users ---")
    add_user("Charlie", "charlie@example.com")
    add_user("Diana", "diana@example.com")
    add_user("", "") # Invalid input
    add_user("Eve", "eve_no_at_sign.com") # Invalid email
    print("Current users list:", users)
    print("-" * 30)

    # READ examples
    print("\n--- Retrieving Users ---")
    user_1 = get_user_by_id(1)
    if user_1:
        print("Found user 1:", user_1)

    user_3 = get_user_by_id(3) # Assuming Charlie got ID 3
    if user_3:
        print("Found user 3:", user_3)

    user_99 = get_user_by_id(99) # Non-existent user
    get_user_by_id("abc") # Invalid ID type
    print("-" * 30)

    # UPDATE examples
    print("\n--- Updating Users ---")
    update_user_by_id(1, new_name="Alice Smith")
    update_user_by_id(2, new_email="robert@example.com", new_name="Robert")
    update_user_by_id(3, new_name="Charles") # Assuming Charlie got ID 3
    update_user_by_id(99, new_name="Nobody") # Non-existent user
    update_user_by_id(1, new_name="") # Invalid new name
    update_user_by_id(2, new_email="bob_invalid") # Invalid new email
    update_user_by_id(4) # No updates provided
    print("Current users list:", users)
    print("-" * 30)

    # DELETE examples
    print("\n--- Deleting Users ---")
    delete_user_by_id(2)
    delete_user_by_id(99) # Non-existent user
    delete_user_by_id("xyz") # Invalid ID type
    print("Current users list:", users)
    print("-" * 30)

    # Show final list
    print("\n--- Final User List ---")
    for u in users:
        print(u)
    print(f"Next available ID will be: {next_id}")