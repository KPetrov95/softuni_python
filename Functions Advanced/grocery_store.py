def grocery_store(**kwargs):
    receipt = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    result = []

    for item in receipt:
        result.append(f"{item[0]}: {item[1]}")

    return "\n".join(result)




print(grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    ))
