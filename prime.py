import math

def is_prime(num):
    """
    Checks if a number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False 
    if num == 2:
        return True   
    if num % 2 == 0:
        return False  

   
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False  
    return True 

while True:
    try:
        user_input_str = input("Enter a whole number to check if it's prime: ")
        number_to_check = int(user_input_str) 
        break 
    except ValueError:
        print("Invalid input. Please enter a valid whole number (e.g., 7, 29, 100).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")