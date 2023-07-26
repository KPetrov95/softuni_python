first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
total_student_questions = int(input())
time_needed = 0
questions_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
while total_student_questions > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    total_student_questions -= questions_per_hour

print(f'Time needed: {time_needed}h.')
