# PAUSE 1 - What is 10 % 3? ANSWER: 1
print(10 % 2)

# PAUSE 2 - Check Odd or Even
user_input = int(input("Enter a number to check if it is even or odd\n"))

# user_input ,class 'str'>
# print(type(user_input)) --> converted to int above

if user_input % 2 != 0:
    print("The number you gave is odd!")
else:
    print("The number you gave is even!")