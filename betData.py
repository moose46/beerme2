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
    def __init__(self) -> None:
        self.individual_bets = defaultdict()
        # self.individual_bets.setdefault("missing_key")
        self.individual_bets["02-19-2023"] = {
            "Greg": "Kyle Larson",
            "Bob": "Ryan Blaney",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["02-26-2023"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Joey Logano",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-05-2023"] = {
            "Greg": "Kyle Larson",
            "Bob": "Kyle Busch",
            "badge_color": "bg-warning text-dark",
        }

        self.individual_bets["03-12-2023"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-19-2023"] = {
            "Greg": "Kyle Busch",
            "Bob": "Joey Logano",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-26-2023"] = {
            "Greg": "Tyler Reddick",
            "Bob": "Ross Chastain",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-02-2023"] = {
            "Greg": "Kyle Larson",
            "Bob": "Kevin Harvick",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-09-2023"] = {
            "Greg": "Kyle Larson",
            "Bob": "Tyler Reddick",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-16-2023"] = {
            "Greg": "William Byron",
            "Bob": "Tyler Reddick",
            "badge_color": "bg-warning text-dark",
        }
        # start of can't pick a driver twice
        self.individual_bets["04-23-2023"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Aric Almirola",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["04-30-2023"] = {
            "Greg": "Kyle Larson",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-07-2023"] = {
            "Greg": "William Byron",
            "Bob": "Martin Truex Jr.",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-14-2023"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Kyle Larson",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-28-2023"] = {
            "Greg": "Chase Elliott",
            "Bob": "Kyle Busch",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-04-2023"] = {
            "Greg": "Kevin Harvick",
            "Bob": "Joey Logano",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-11-2023"] = {
            "Greg": "Tyler Reddick",
            "Bob": "AJ Allmendinger",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-25-2023"] = {
            "Greg": "Martin Truex Jr.",
            "Bob": "Ross Chastain",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-02-2023"] = {
            "Greg": "Christopher Bell",
            "Bob": "Shane van Gisbergen",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-09-2023"] = {
            "Greg": "Joey Logano",
            "Bob": "Ryan Blaney",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-17-2023"] = {
            "Greg": "Aric Almirola",
            "Bob": "Bubba Wallace",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-23-2023"] = {
            "Greg": "Austin Cindric",
            "Bob": "Christopher Bell",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-30-2023"] = {
            "Greg": "Ty Gibbs",
            "Bob": "Chase Elliott",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["08-06-2023"] = {
            "Greg": "Ross Chastain",
            "Bob": "Kevin Harvick",
            "badge_color": "bg-success text-light",
        }

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet indate_formation for Greg and Bob
        """
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
            bets.append(
                Bet(
                    race_date=data.DATE,  # type: ignore
                    track=data.TRACK,  # type: ignore
                    player=data.PLAYER,  # type: ignore
                    driver=data.DRIVER,  # type: ignore
                )
            )
    # for x in sorted(bets):
    #     print(x)
    # create a unique set of race dates
    # for x in bets:
    #     race_dates.add(x.race_date)

    # create a a list of unique dates
    all_race_dates = {x.race_date for x in bets}
    for d in all_race_dates:
        # print(f"{d:%m-%d-%Y}")
        race_bets = [x for x in bets if x.race_date == d]
        print(f"{race_bets[0]}\n{race_bets[1]}\n")
        file_names = results_file_path.glob(f"results_*{d:%m-%d-%Y}_.txt")
        for fname in file_names:
            with open(fname):
                print(f"found {d:%m-%d-%Y} ok!")
    #     print([y for y in bets if y.race_date == x])

    # abet = [
    #     bet
    #     for bet in bets
    #     if bet.race_date == datetime.datetime.strptime("04-23-2023", date_format)
    # ]
    # print(abet)
