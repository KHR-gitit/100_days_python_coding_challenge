#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split_into = int(input("How many people to split the bill?"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
pay = round((bill + (bill * (tip / 100))) / split_into, 2)
print(f"Each person should pay: ${pay}")