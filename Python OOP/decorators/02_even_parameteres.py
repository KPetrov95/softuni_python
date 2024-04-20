def even_parameters(function):
    def wrapper(*args, **kwargs):
        if any(not isinstance(x, int) or x % 2 != 0 for x in args):
            return "Please use only even numbers!"
        return function(*args, **kwargs)
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
