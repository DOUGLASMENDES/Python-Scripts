# Authors: Aman Kharval / Douglas Mendes
# Source: 
#   https://thecleverprogrammer.com/2020/08/17/password-generator-with-python/
#   96 Python Projects with Source Code
#   https://medium.com/coders-camp/96-python-projects-with-source-code-4069eb58beef

import random


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Enter Password length (min 4 characters): "))

include_special = input("Include special characters? (y | n)  ")
if include_special.capitalize() == 'Y':
    special = ",.<>:\/{}[]+=-_?!@#$%&amp;*"
    characters = characters + special

if length < 4: length = 4

for i in range(1,10):
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print(password)