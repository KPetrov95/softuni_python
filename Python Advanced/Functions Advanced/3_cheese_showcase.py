def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for name, quantity in sorted_dict:
        result += f"{name}\n"
        sorted_quantities = sorted((quantity), reverse=True)
        for element in sorted_quantities:
            result += f"{element}\n"

    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
