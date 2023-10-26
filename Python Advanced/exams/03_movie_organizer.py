def movie_organizer(*args):
    movies_names_dict = {}
    result = []

    for name, genre in args:
        if genre not in movies_names_dict:
            movies_names_dict[genre] = []
        movies_names_dict[genre].append(name)
    sorted_dict = sorted(movies_names_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for genre, names in sorted_dict:
        result.append(f'{genre} - {len(names)}')
        for current_movie in sorted(names):
            result.append(f'* {current_movie}')
    return f"\n".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
