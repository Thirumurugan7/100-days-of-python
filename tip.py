print("Wlcome to the tip calculator.")
bill = float(input("What was the total bill?"))

tip_percent = int(input("What percentage tip would you like to give? 10,12, or 15?"))

split_bill= int(input("How many people to split the bill?"))

interest=(bill*(12/100))
a=bill+interest
amount = a/split_bill

last = round(amount,2) 

print(f"Each person should pay: ${last}")
