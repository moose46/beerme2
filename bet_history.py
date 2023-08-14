# bet_history.py
from betData import BetData

data = BetData()


all_bets = data.get_bets


def look_driver_up(player_name: str, driver_name: str) -> bool:
    return any(
        race_date >= "04-23-2023" and all_bets[race_date][player_name] == driver_name
        for race_date in all_bets
    )


for race_date in all_bets:
    if race_date < "04-23-2023":
        continue
    for player_name in all_bets[race_date]:
        if player_name != "badge_color":
            is_avaiable = look_driver_up(player_name, all_bets[race_date][player_name])
            print(f"{player_name:6s} {is_avaiable}", end=" = ")
            print(
                f"{'Available' if is_avaiable == False else 'Picked'} {all_bets[race_date][player_name]:16s}",
            )
    print()


print(f'{look_driver_up("Bob", "Ryan Blaney")}')
print(f'{look_driver_up("Bob", "Tyler Reddick")}')
print(f'{look_driver_up("Bob", "Denny Hamlin")}')


print(
    any(
        race_date >= "04-23-2023" and all_bets[race_date]["Bob"] == "Tyler Redddick"
        for race_date in all_bets
    )
)
