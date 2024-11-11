import random
import os

# main logic
def pwd_generator(num, len_of_chars):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz1234567890~`!@#$%^&*()-_+={}[]|\\;:\"<>,./?"
    for i in range(num):
        password = ""
        for j in range(len_of_chars):
            password += random.choice(characters)
        print(password)



# clearing the terminal
os.system('cls||clear')
print("Password Generator")
print("-------")
print("Based on Princeton University's advice on selecting good passwords.")
print("Read more at https://csguide.cs.princeton.edu/accounts/passwords")
print("-------")
print()

# taking the user's input
num = -1
len_of_chars = -1
while num < 1 and len_of_chars < 10:
    
    # validate number of passwords
    while num < 1:
        try:
            num = int(input("Number of passwords needed: "))
        except:
            continue
    
    # validate number of characters
    while len_of_chars < 10:
        try:
            len_of_chars = int(input("Characters per password (> 9): "))
        except:
            continue

print()

pwd_generator(num, len_of_chars)
print()