grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]

students = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
}

students_list = list(students)
students_list.sort()

avg_grades = (
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])
)

'''
# общее решение, но lambda в пройденном материале ещё не было
avg_grades = list(map(
    lambda student_grades:
        sum(student_grades) / len(student_grades),
    grades
))
'''

students_avg_grade = dict(zip(students_list, avg_grades))
print(students_avg_grade)
