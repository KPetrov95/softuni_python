def age_assignment(*args, **kwargs):
    person = {}
    result = []
    for name in args:
        person[name] = kwargs[name[0]]

    for key, value in sorted(person.items()):
        result.append(f'{key} is {value} years old.')
    return "\n".join(result)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print()
print(age_assignment("Peter", "George", G=26, P=19))