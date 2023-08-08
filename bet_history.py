# bet_history.py
from betData import BetData

data = BetData()


all_bets = data.get_bets


def look_driver_up(driver_key_name):
    return True


for race_date in all_bets:
    if race_date >= "04-23-2023":
        print(f"{race_date}", end=" - ")
        for key_name in all_bets[race_date]:
            if key_name != "badge_color":
                print(f"{all_bets[race_date]['Bob']:6s}", end=" ")
                print(
                    f"{look_driver_up(key_name)} {all_bets[race_date][key_name]:16s}",
                    end=" - ",
                )
    print()
