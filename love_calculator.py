# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1=name1.lower()
n2=name2.lower()
t=n1.count("t")
r=n1.count("r")
u=n1.count("u")
e=n1.count("e")
t2=n2.count("t")
r2=n2.count("r")
u2=n2.count("u")
e2=n2.count("e")

l=n1.count("l")
o=n1.count("o")
v=n1.count("v")
e=n1.count("e")
l2=n2.count("l")
o2=n2.count("o")
v2=n2.count("v")
e2=n2.count("e")

t1=t+r+u+e+t2+r2+u2+e2
t2=l+o+v+e+l2+o2+v2+e2
t=str(t1)+str(t2)

res=int(t)
if(res<10 or res>90):
    print(f"your score is {res}, you go together like coke and mentos")
elif(res>40 and res<50):
    print(f"Your score is {res}, you are alright together.")    
else:
    print(f"your score is{res}.")