print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0


if size == "S":
    pizza_price += 15
    if pepperoni == "Y":
        pizza_price += 2
elif size == "M":
    pizza_price += 20
    if pepperoni == "Y":
        pizza_price += 3
elif size == "L":
    pizza_price += 25
    if pepperoni == "Y":
        pizza_price += 3
if extra_cheese == "Y":
    pizza_price += 1
print(f"Your final bill is: ${pizza_price}.")


# Solution Below
# # todo: work out how much they need to pay based on their size choice.
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You have chosen an invalid size.")
#
# # todo: work out how much to add to their bill based on their pepperoni choice.
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# # todo: work out their final amount based on whether if they want extra cheese.
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")