import re

def is_valid_email(email):
    """
    Checks if an email is valid using regex based on the format username@domain.com.
    - username: letters, numbers, and common special characters (._%+-).
    - domain: letters, numbers, dots, hyphens.
    - TLD (Top-Level Domain like .com): At least two letters.
    """
    if not isinstance(email, str):
        return False # Email must be a string

    # Regex pattern for username@domain.tld
    # - ^ : asserts position at start of the string
    # - [a-zA-Z0-9._%+-]+ : username part (one or more alphanumeric or . _ % + -)
    # - @ : literal @ symbol
    # - [a-zA-Z0-9.-]+ : domain part (one or more alphanumeric or . -)
    # - \. : literal . symbol (must be escaped)
    # - [a-zA-Z]{2,} : TLD part (at least two letters)
    # - $ : asserts position at the end of the string
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # re.fullmatch checks if the entire string matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

# --- Example Usage as per the Task ---
if __name__ == "__main__":
    print("--- Email Validation Task ---")

    email1 = "user@domain.com"
    result1 = is_valid_email(email1)
    print(f'is_valid_email("{email1}")  # Output: {result1}') # Expected: True

    email2 = "user@domain" # Missing .com (or a TLD)
    result2 = is_valid_email(email2)
    print(f'is_valid_email("{email2}")  # Output: {result2}') # Expected: False

    print("\n--- Additional Test Cases ---")
    # Valid emails
    print(f'is_valid_