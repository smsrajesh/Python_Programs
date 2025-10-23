student_marks={}
n=int(input("How many values you want to Enter : "))
for i in range(n):
    key=input("Enter the Key : ")
    value=int(input("Enter the Value : "))
    student_marks[key]=value
    

print(student_marks)


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



# OUTPUT

# How many values you want to Enter : 5
# Enter the Key : Rajesh
# Enter the Value : 95
# Enter the Key : Mani
# Enter the Value : 88
# Enter the Key : Shanmukha
# Enter the Value : 76
# Enter the Key : Sankara
# Enter the Value : 63
# Enter the Key : Raju
# Enter the Value : 35
# {'Rajesh': 95, 'Mani': 88, 'Shanmukha': 76, 'Sankara': 63, 'Raju': 35}
# Rajesh 95
# Mani 88
# Shanmukha 76
# Sankara 63
# Raju 35
# {'Rajesh': 'A+', 'Mani': 'A', 'Shanmukha': 'B+', 'Sankara': 'B', 'Raju': 'Fail'}
 


student_marks = {}

n = int(input("How many values you want to Enter : "))

for i in range(n):
    key = input("Enter the Student Name : ")
    value = int(input("Enter the Marks : "))
    student_marks[key] = {"marks": value}   # store marks first

for name in student_marks.keys():
    marks = student_marks[name]["marks"]
    grade = ""

    if marks > 100:
        grade = 'Not Valid'
    elif marks in range(91, 101):
        grade = 'A+'
    elif marks in range(81, 91):
        grade = 'A'
    elif marks in range(71, 81):
        grade = 'B+'
    elif marks in range(61, 71):
        grade = 'B'
    elif marks in range(51, 61):
        grade = 'C'
    elif marks in range(41, 51):
        grade = 'D'
    else:
        grade = 'Fail'

    # Add grade to the same student entry
    student_marks[name]["grade"] = grade

print("\nFinal Student Records:")
for name, info in student_marks.items():
    print(f"{name} -> Marks: {info['marks']}, Grade: {info['grade']}")

print("\nDictionary Format:")
print(student_marks)



# Final Student Records:
# Rajesh -> Marks: 95, Grade: A+
# Mani -> Marks: 82, Grade: A
# Shanmukha -> Marks: 68, Grade: B
# Raju -> Marks: 39, Grade: Fail

# Dictionary Format:
# {'Rajesh': {'marks': 95, 'grade': 'A+'},
#  'Mani': {'marks': 82, 'grade': 'A'},
#  'Shanmukha': {'marks': 68, 'grade': 'B'},
#  'Raju': {'marks': 39, 'grade': 'Fail'}}
