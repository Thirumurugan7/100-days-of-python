import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)
random_pay = random.randint(0,len(names)-1)

payer=names[random_pay]

print(f"{payer} going to pay")