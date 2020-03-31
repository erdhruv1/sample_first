def main():
    lst = []
    n = int(input())
    for i in range(n):
        l = [input(), float(input())]
        lst.append(l)

    grades = {}

    for i in lst:
        grades[i[0]] = i[1]

    marks = set((grades.values()))
    sorted_marks = sorted(marks)

    second_lowest_mark = sorted_marks[1]

    final_student_list = []

    for i in lst:
        if second_lowest_mark == i[1]: # i[1] represents only marks in list of lists
            final_student_list.append(i[0])  # i[0] represents only names in the list of lists

    for i in final_student_list:
        print(i)

if __name__ == '__main__':
    main()