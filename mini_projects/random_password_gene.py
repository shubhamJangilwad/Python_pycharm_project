import random

len_password = int(input("Enter password length: "))
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$&"
password = ''

if 6 < len_password < 12:
    for i in range(len_password):
        random_char = random.choice(characters)
        password = password + random_char
    print(password)

else:
    print("invalid password")



