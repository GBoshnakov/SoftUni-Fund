def validate_password(passw):
    is_Valid = True
    is_letters_and_digits = True
    if not 6 <= len(passw) <= 10:
        print("Password must be between 6 and 10 characters")
        is_Valid = False


    counter_letters = 0

    for l in passw:
        if (ord(l) < 48) or (58 >= ord(l) >= 64) or (91 >= ord(l) >= 96) or (ord(l) >= 123):
            is_letters_and_digits = False
            is_Valid = False

        if 48 <= ord(l) <= 57:
            counter_letters += 1
    if not is_letters_and_digits:
        print("Password must consist only of letters and digits")
    if counter_letters < 2:
        is_Valid = False
        print("Password must have at least 2 digits")
    if is_Valid:
        print("Password is valid")

password = input()

validate_password(password)