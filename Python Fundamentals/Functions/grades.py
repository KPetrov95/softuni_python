def grade_to_score(some_grade):
    resulting_score = ''
    if 2.00 <= some_grade <= 2.99:
        resulting_score = "Fail"
    elif 3.00 <= some_grade <= 3.49:
        resulting_score = "Poor"
    elif 3.50 <= some_grade <= 4.49:
        resulting_score = "Good"
    elif 4.50 <= some_grade <= 5.49:
        resulting_score = "Very Good"
    elif 6.00 >= some_grade >= 5.50:
        resulting_score = "Excellent"
    return resulting_score


grade = float(input())
result = grade_to_score(grade)
print(result)
