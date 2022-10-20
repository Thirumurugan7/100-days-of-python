#sum of even numbers from 2 to 100  👇
sumf=0
for i in range(1,101):
  if(i%2 == 0):
    sumf+=i
print(f"the sumis {sumf}")    