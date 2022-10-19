import random

random_coin = random.randint(0,1)
if(random_coin == 0):
  ht="Tails"
else:
  ht="Heads"
print(f"Its {ht}")