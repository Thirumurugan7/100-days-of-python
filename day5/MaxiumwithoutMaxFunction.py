
student_scores = input("Input a list of student scores"). split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])




flag=0
for h in student_scores:
  if (h>flag):
    flag=h
print(flag)   
