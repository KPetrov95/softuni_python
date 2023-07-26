team_a = ["A-" + str(s) for s in range(1,12)]
team_b = ['B-' + str(s) for s in range(1,12)]
send_off_players = input().split()
game_terminated = False

for player in send_off_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_terminated:
    print("Game was terminated")
