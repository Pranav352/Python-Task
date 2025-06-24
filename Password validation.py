# password validation
# password=

# Get password input from the user
password = input("Enter your password: ")

# Criteria 
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*()-_+=<>?"

# length of the password
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    # Iterate through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Check if all criteria are true
    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
    else:
        print("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

