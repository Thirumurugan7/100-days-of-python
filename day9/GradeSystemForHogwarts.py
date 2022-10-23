student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

grades={}


for key in student_scores:
	if((student_scores[key] >= 91) & (student_scores[key] <=100 )):
		grades[key]="Outstanding"
	elif((student_scores[key] >= 81) & (student_scores[key] <=90 )):
		grades[key]="Exceeds Expectation"
	elif((student_scores[key] >=71) & (student_scores[key] <=80)):
		grades[key]="acceptable"
	else:
		grades[key]="Fail"




print(grades)





