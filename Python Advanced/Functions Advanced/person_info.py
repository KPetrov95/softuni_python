def get_info(age, town, name):
    return f"This is {name} from {town} and he is {age} years old"


kwargs = {"name": "John", "town": "Sofia", "age": 20}
print(get_info(**kwargs))
