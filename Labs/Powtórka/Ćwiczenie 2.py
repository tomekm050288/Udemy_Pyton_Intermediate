valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}\|;:?/>.<,'


def checker(password):
    lst = []
    for letter in password:
        if letter in valid_characters and len(password) > 8:
            lst.append(letter)
        else:
            print("Error! Password not valid")
            return False
    else:
        return True

print(checker('~dsdsdsdsdsdsdsdsd'))
