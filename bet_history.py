# bet_history.py
from betData import BetData

data = BetData()


all_bets = data.get_bets


def look_driver_up(race_date,player_name,driver_name):
    if player_name == 'Bob':
        player_name = 'Greg'
    else:
        player_name = 'Bob'
    print(f'\nplayer_name={player_name}, driver_name={driver_name}')
    # return all_bets[race_date][player_name] == driver_name
    for x in all_bets[race_date]:
        if x == "badge_color":
            continue
        print(f'x={x}')
        if all_bets[race_date][x] == driver_name:
            return True
    return False
    return [x for x in all_bets[race_date][player_name] if x == driver_name]


for race_date in all_bets:
    if race_date >= "04-23-2023":
        print(f"{race_date}", end=" - ")
        for player_name in all_bets[race_date]:
            if player_name != "badge_color":
                print(f"{player_name:6s}", end=" = ")
                print(
                    f"{look_driver_up(race_date,player_name, all_bets[race_date][player_name])} {all_bets[race_date][player_name]:16s}",
                )
    print()
