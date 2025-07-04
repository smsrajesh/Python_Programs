student_marks={}
n=int(input("How many values you want to Enter : "))
for i in range(n):
    key=input("Enter the Key : ")
    value=int(input("Enter the Value : "))
    student_marks[key]=value
    

print(student_marks)

student_grade=dict()
for i in student_marks.keys():
    print(i,student_marks[i])
    grade = ""
    if student_marks[i]>100:
        grade='Not Valid'
    elif student_marks[i] in range(91,101):
        grade='A+'
    elif student_marks[i] in range(81,91):
        grade='A'
    elif student_marks[i] in range(71,81):
        grade='B+'
    elif student_marks[i] in range(61,71):
        grade='B'
    elif student_marks[i] in range(51,61):
        grade='C'
    elif student_marks[i] in range(41,51):
        grade='D'
    else:
        grade='Fail'
    student_marks[i]=grade

print(student_marks)

