def gather_credits(credits_needed, *courses):
    obtained_credits = 0
    completed_courses = []
    for name, course_score in courses:
        if obtained_credits >= credits_needed:
            break
        if name in completed_courses:
            continue
        obtained_credits += course_score
        completed_courses.append(name)
    if obtained_credits >= credits_needed:
        return (f"Enrollment finished! Maximum credits: {obtained_credits}.\n"
                f"Courses: {', '.join(sorted(completed_courses))}")
    return f"You need to enroll in more courses! You have to gather {credits_needed - obtained_credits} credits more."


print(gather_credits(
    60,
    ("Basics", 27),
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
print()
print(gather_credits(
    80,
    ("Basics", 27),
))
