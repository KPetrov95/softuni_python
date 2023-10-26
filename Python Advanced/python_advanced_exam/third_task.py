def team_lineup(*args):
    teams_dict = {}
    result = []
    for player, country in args:
        if country not in teams_dict:
            teams_dict[country] = []
        teams_dict[country].append(player)
    sorted_dict = sorted(teams_dict.items(), key=lambda x:(-len(x[1]), x[0]))

    for team, names in sorted_dict:
        result.append(f'{team}:')
        for current_player in names:
            result.append(f"  -{current_player}")
    return f"\n".join(result)

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

