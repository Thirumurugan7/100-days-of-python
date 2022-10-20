
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):

  student_heights[n] = int(student_heights[n])

a=0
noofstud=0
for b in student_heights:
  noofstud +=1

for i in student_heights:
  
  a+=i
  
print("average",round(a/noofstud))
