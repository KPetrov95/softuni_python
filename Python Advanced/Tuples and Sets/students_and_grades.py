n = int(input())

students_grades = {}

for _ in range(n):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for key, value in students_grades.items():
    average = sum(value) / len(value)
    formatted_grades = " ".join([f'{x:.2f}'for x in value])
    print(f'{key} -> {formatted_grades} (avg: {average:.2f})')