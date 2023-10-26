def get_magic_triangle(num):
    triangle = [[1], [1, 1]]
    for i in range(num - 2):
        row = triangle[-1].copy()
        default_row = triangle[1].copy()
        for j in range(i + 1):
            default_row.insert(1, (row[j] + row[j + 1]))
        triangle.append(default_row)
    return(triangle)


get_magic_triangle(5)