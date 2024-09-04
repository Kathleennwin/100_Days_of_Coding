# PAUSE 1. Fix the len() function so it has no more warnings or errors.
len("12345")

# PAUSE 2. Write out 4 type checks to print all 4 data types
print(type("123"))
print(type(12.2))
print(type(12))
print(type(True))

# PAUSE 3. Make this line of code run without errors
# print(type(len(input("Enter your name"))))
print("Number of letters in your name: " + str(len(input("Enter your name"))))