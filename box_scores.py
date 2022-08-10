bulls = {
    'name':'Durham Bulls',
    'players': ('B', 'M', 'A', 'P', 'G', 'W', 'B', 'E', 'H'),
    'runs': 0,
}

shrimp = {
    'name':'Jax Jumbo Shrimp',
    'players': ('B', 'A', 'S', 'E', 'A', 'H', 'G', 'M', 'G'),
    'runs': 0,
}

last_night_game = {
    'teams': (bulls, shrimp),
    'date': '2022-08-09',
    'winner': None
}


def get_game_score(game):
    team1 = game['teams'][0]
    team2 = game['teams'][1]
    return (f"""The score is:
    {team1['name']}, {team1['runs']}
    {team2['name']}, {team2['runs']}""")


# first inning
bulls['runs'] += 3
shrimp['runs'] += 1

# second inning
bulls['runs'] += 0
shrimp['runs'] = shrimp['runs'] + 0

print(get_game_score(last_night_game))
