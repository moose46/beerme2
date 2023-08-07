# bet_history.py
from betData import BetData

data = BetData()

all_bets = data.get_bets

for race_date in all_bets:
    print(f"{race_date}")
    for name in all_bets[race_date]:
        print(name)
