print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


# Figuring out the type of the variables so I know what I am working with
# print(type(bill))
# print(type(tip))
# print(type(people))


bill_tip = tip / 100 * bill
total_bill = bill_tip + bill
bill_per_person = round(total_bill / people, 2)

print(f"Each person has to pay: $ {bill_per_person:.2f}" )

