import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listing=[rock,paper,scissors]
entry1=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
entry=int(entry1)
print(listing[entry])

computer_entry=random.randint(0,2)

print(computer_entry)
print(listing[computer_entry])

if((entry==0) & (computer_entry==1)):
  print("computer wins")
elif((entry==1) & (computer_entry==2)):
  print("c won")
elif((entry==2) & (computer_entry==0)):
  print("computer wins")  
elif(entry==computer_entry):
  print("try again its a tie")
else:
  print("human wins")