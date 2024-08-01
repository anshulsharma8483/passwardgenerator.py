import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    # Define character sets based on user preferences
    characters = []
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_lowercase:
        characters.extend(string.ascii_lowercase)
    if include_digits:
        characters.extend(string.digits)
    if include_special:
        characters.extend(string.punctuation)
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    print("Specify the parameters for your password:")
    
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
    
    print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
