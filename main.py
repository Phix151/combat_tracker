from player import Player

players = {}

def create_player(hp, name, st=10, dex=10, const=10, intelligence=10, wis=10, char=10, ac=10):
    player = Player(hp, name, st, dex, const, intelligence, wis, char, ac)
    players[name] = player

def set_init(name, init):
    players[name].set_init(init)

def group_init(group, init):
    for player in players:
        if players[player].get_group() == group:
            players[player].set_init(init)


