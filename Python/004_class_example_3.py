class team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def __getitem__(self, i):
        return self.players[i]
    def __str__(self):
        return f'{self.players}'


team1 = team('team1')
team1.players.append("Toto")
team1.players.append("Tata")

for player in team1:
    print (player)
print(team1.name)

print (team1)
