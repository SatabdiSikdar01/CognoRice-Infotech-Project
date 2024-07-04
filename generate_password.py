import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Start with lowercase characters
    characters = lower
    
    # Add other character sets based on user preferences
    if use_uppercase:
        characters += upper
    if use_numbers:
        characters += digits
    if use_special:
        characters += special

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    # Prompt user for the desired password length
    length = int(input("Enter the desired length of the password: "))

    # Prompt user for complexity preferences
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print(f"Generated password: {password}")

# Run the password generator
password_generator()
