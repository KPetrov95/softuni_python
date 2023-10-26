def students_credits(*args):
    NEEDED_CREDITS = 240
    total_credits = 0
    dict_courses = {}
    result = []
    for arg in args:
        course_name, course_credits, max_points, current_points = [x for x in arg.split('-')]
        credits_for_course = (float(current_points)/float(max_points)) * float(course_credits)
        total_credits += credits_for_course
        dict_courses[course_name] = credits_for_course
    if total_credits >= NEEDED_CREDITS:
        result.append(f'Diyan gets a diploma with {total_credits:.1f} credits.')
    else:
        result.append(f'Diyan needs {NEEDED_CREDITS - total_credits:.1f} credits more for a diploma.')
    sorted_dict = sorted(dict_courses.items(), key=lambda kvp: -kvp[1])
    for key, value in sorted_dict:
        result.append(f'{key} - {value:.1f}')
    return '\n'.join(result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)



