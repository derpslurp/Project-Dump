import random
import string


def generate_password(min_l, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_l:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd

while True:
    start = input('Press any key to start or q to quit: ')
    if start == 'q':
        break
    else:
        length = input('What is the minimum length you would like you password to be?:  ')
        if length.isdigit():
            length = int(length)
        else:
            print('Invalid input')
            continue
        pwd = generate_password(length)
        print(pwd)
