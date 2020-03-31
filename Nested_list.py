number_of_students = int(input("Enter the number of students: "))

student_name = []
marks = []

for _ in range(number_of_students):
    student_name.append(input())
    marks.append(input())

student_marks_list = list(zip(student_name, marks))

grades = {}

for j in range(0, number_of_students):
    grades[student_marks_list[j][0]] = student_marks_list[j][1]

sorted_marks_list = (sorted(set(grades.values())))

marks_to_match = sorted_marks_list[1]

result = []

for name in grades.keys():
    if grades[name] == marks_to_match:
        result.append(name)

for k in result:
    print(k)