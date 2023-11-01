list_of_courses = []
course_to_search = ''
while True:
    command = input()
    if ':' not in command:
        course_to_search = command
        break
    name, ID, course = command.split(':')
    list_of_courses.append({"name": name, "ID": ID, "course": course})

for current_course in list_of_courses:
    if course_to_search.startswith(current_course["course"][0:3]):
        print(f"{current_course['name']} - {current_course['ID']}")
