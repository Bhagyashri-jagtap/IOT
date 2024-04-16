''' The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F'''


sub1=int(input("enter subject 1 marks"))

sub2=int(input("enter subject 2 marks"))

sub3=int(input("enter subject 3 marks"))

avg_marks= (sub1+sub2+sub3)/3
print(f"Average marks = {avg_marks}")

if avg_marks >=90:
	print("Grade A")

elif avg_marks >=80:
	print("Grade B")

elif avg_marks >=70:
	print("Grade C")

elif avg_marks >=60:
	print("Grade D")

else :
	print("fail")


