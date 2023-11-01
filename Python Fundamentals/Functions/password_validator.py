def length_validator(some_password : str) -> bool:
    if len(some_password) in range(6, 11):
        return True
    return False


def character_validator(some_password : str) -> bool:
    if some_password.isalnum():
        return True
    return False


def digits_validator(some_password : str) -> bool:
    digits_counter = 0
    for char in some_password:
        if char.isdigit():
            digits_counter +=1
    if digits_counter >= 2:
        return True
    return False


password = input()

password_verification = [length_validator(password), character_validator(password),digits_validator(password)]

if all(password_verification):
    print("Password is valid")
if not password_verification[0]:
    print("Password must be between 6 and 10 characters")
if not password_verification[1]:
    print("Password must consist only of letters and digits")
if not password_verification[2]:
    print("Password must have at least 2 digits")
