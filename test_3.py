students={}
number_of_students=int(input("Enter the number of students: "))
for i in range(number_of_students):
    name=input("Enter the name of student: ")
    marks=int(input("Enter marks for student: "))
    students[name]=marks

print("Student record: ",students)
total_marks=0
for name in students:
    total_marks=total_marks+students[name]

avg=total_marks/number_of_students
print("Average: ",avg)

highest_score=max(students,k=students.get)
print("Highest Score: ",highest_score)