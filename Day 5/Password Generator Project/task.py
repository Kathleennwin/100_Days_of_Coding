import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# EASY VERSION
# password = ""
#SOLUTION USES +=
# for char in range(1, nr_letters + 1):
#     password = password + random.choice(letters)
#     print(password)
# for num in range(1, nr_numbers + 1):
#     password = password + random.choice(numbers)
#     print(password)
# for sym in range(1, nr_symbols + 1):
#     password = password + random.choice(symbols)
#     print(password)

# HARD VERSION
password = []
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))
    # print(password)
for num in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
    # print(password)
for sym in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
    # print(password)

# Shuffle password for higher strength/security
random.shuffle(password)
print(password)

# Using sum of user's desired password length to later create the range or number of cycles for the FOR loop
password_total_length = nr_symbols + nr_numbers + nr_letters
# empty string to print once finished
password_String =""
index = 0
# Turn password list into a string
for characters in range(1, password_total_length + 1):
    password_String += password[index]
    index+=1
print("Here is your new password: " + password_String)