def rectangle(length, width):
    if not isinstance(width, int) or not isinstance(length, int):
        return "Enter valid values!"
    return f"Rectangle area: {length * width}\nRectangle perimeter: {2* (length + width)}"


print(rectangle(2, 10))

print(rectangle('2', 10))