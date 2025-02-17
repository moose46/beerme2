# betting data goes here
# import the datetime module
import csv
import datetime
from collections import defaultdict, namedtuple
from datetime import date
from operator import itemgetter
from pathlib import Path
from string import capwords

# datetime in string date_format for may 25 1999
# input = "2021/05/25"

# date_format
# date_format = '%Y/%m/%d'
date_format = "%m-%d-%Y"
# convert from string date_format to datetime date_format

# get the date from the datetime using date()
# function
# print(datetime.date())


class BetData:
    def __getitem__(self, race_date):
        return self.individual_bets[race_date]

    def __init__(self) -> None:
        self.individual_bets = defaultdict()
        # self.individual_bets.setdefault("missing_key")
        self.individual_bets["02-16-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "Track": "Daytona",
            "badge_color": "bg-warning text-dark",
        }

        # # start of can't pick a driver twice

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet in date_information for Greg and Bob
            first pick starts at the first of the year and alternates each week
        """
        for first_pick, x in enumerate(self.individual_bets):
            self.individual_bets[x]["first_pick"] = "Greg" if first_pick % 2 else "Bob"
        return self.individual_bets


class Bet(object):
    def __init__(
        self,
        race_date: date,
        track: str,
        player: str,
        driver: str,
        badge_color="bg-warning text-dark",
    ) -> None:
        self.race_date = datetime.datetime.strptime(race_date, date_format)

        self.track = capwords(track)
        self.player = player
        self.driver = driver
        self._finish = -1
        # after this date we can not pick the same driver twice
        self.badge_color = (
            "bg-warning text-dark"
            if self.race_date < datetime.datetime.strptime("04-23-2023", date_format)
            else "bg-success text-light"
        )
        # print(self.race_date < datetime.datetime.strptime("04-23-2023", date_format))

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, position):
        self._finish = position

    def __lt__(self, other):
        return (self.race_date) < (other.race_date)

    def __gt_(self, other):
        return (self.race_date) > (other.race_date)

    def __eq_(self, other):
        return (self.race_date) == (other.race_date)

    def __le_(self, other):
        return (self.race_date) <= (other.race_date)

    def __ge_(self, other):
        return (self.race_date) >= (other.race_date)

    def __repr__(self) -> str:
        return f"{self.race_date:%m-%d-%Y} {self.track} {self.player} {self.driver} {self.finish} {self.badge_color}"


file_path = Path.cwd() / "data" / "betData.csv"
results_file_path = Path.cwd() / "data"

if __name__ == "__main__":
    """to test: python betData.py"""
    bets = []
    race_dates = set()
    # print(f"race_dates = {type(race_dates)}")
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        BetInfo = namedtuple("BetInfo", next(reader), rename=True)
        data = []
        for header in reader:
            try:
                data = BetInfo(*header)
            except Exception as e:
                print(e)
                exit()
            bets.append(
                Bet(
                    race_date=data.DATE,  # type: ignore
                    track=data.TRACK,  # type: ignore
                    player=data.PLAYER,  # type: ignore
                    driver=data.DRIVER,  # type: ignore
                )
            )
    print(f"Number of Races = {len(bets) // 2}")
    # for x in sorted(bets):
    #     print(x)
    # create a unique set of race dates
    # for x in bets:
    #     race_dates.add(x.race_date)

    # create a a list of unique dates
    # all_race_dates = {x.race_date for x in bets}
    # for d in all_race_dates:
    #     print(f"{d:%m-%d-%Y}")
    #     race_bets = [x for x in bets if x.race_date == d]
    #     print(f"{race_bets[0]}\n{race_bets[1]}\n")
    #     file_names = results_file_path.glob(f"results_*{d:%m-%d-%Y}_.txt")
    #     for fname in file_names:
    #         with open(fname):
    #             print(f"found {d:%m-%d-%Y} ok!")
    #     print([y for y in bets if y.race_date == x])

    # abet = [
    #     bet
    #     for bet in bets
    #     if bet.race_date == datetime.datetime.strptime("04-23-2023", date_format)
    # ]
    # print(abet)
    import glob
    import os

    """
        To run: run python betData.py
        this will check to see if betData race dates match the data race dates in the data subdirectory

        Output:
        a list of dates and if the data file does not exist, the date will have false next to the race date

        Example:
        03-24-2022 False # file not found
        03-17-2022 True # file was found
    """
    all_bets = BetData()
    first_pick = 0
    for x in all_bets.get_bets:
        file_path = Path.cwd() / "data"
        fn = f"{file_path}/*_{x}_.txt*"
        print(f"{x} Race Data File {fn} Found: {not not glob.glob(fn)}")
        # if first_pick % 2:
        #     all_bets[x]["first_pick"] = "Greg"
        # else:
        #     all_bets[x]["first_pick"] = "Bob"
        # first_pick += 1
        print(all_bets[x])
