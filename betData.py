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
        self.individual_bets["02-18-2024"] = {
            "Greg": "Joey Logano",
            "Bob": "Chase Elliott",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["02-25-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Joey Logano",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-03-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "William Byron",
            "badge_color": "bg-warning text-dark",
        }

        self.individual_bets["03-10-2024"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-17-2024"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Christopher Bell",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-24-2024"] = {
            "Greg": "Chris Buescher",
            "Bob": "William Byron",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-31-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Chris Buescher",
            "badge_color": "bg-warning text-dark",
        }
        # Martinsville
        self.individual_bets["04-07-2024"] = {
            "Greg": "Christopher Bell",
            "Bob": "Martin Truex Jr.",
            "badge_color": "bg-warning text-dark",
        }
        # Texas Cota
        self.individual_bets["04-14-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "William Byron",
            "badge_color": "bg-warning text-dark",
        }
        # Talladega
        self.individual_bets["04-21-2024"] = {
            "Greg": "Brad Keselowski",
            "Bob": "Ryan Blaney",
            "badge_color": "bg-warning text-dark",
        }
        # # start of can't pick a driver twice
        self.individual_bets["04-28-2024"] = {
            "Greg": "Denny Hamlin",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-05-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-12-2024"] = {
            "Greg": "Martin Truex Jr.",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["05-26-2024"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-02-2024"] = {
            "Greg": "Joey Logano",
            "Bob": "Denny Hamlin",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-09-2024"] = {
            "Greg": "Chase Elliott",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-16-2024"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Christopher Bell",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-23-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Ryan Blaney",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["06-30-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-07-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Shane van Gisbergen",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-14-2024"] = {
            "Greg": "Denny Hamlin",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["07-21-2024"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["08-11-2024"] = {
            "Greg": "Christopher Bell",
            "Bob": "Denny Hamlin",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["08-18-2024"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Ross Chastain",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["08-24-2024"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "badge_color": "bg-success text-light",
        }
        self.individual_bets["09-01-2024"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Tyler Reddick",
            "badge_color": "bg-success text-light",
        }
        # self.individual_bets["08-06-2023"] = {
        #     "Greg": "Ross Chastain",
        #     "Bob": "Kevin Harvick",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["08-13-2023"] = {
        #     "Greg": "Shane van Gisbergen",
        #     "Bob": "Daniel Suarez",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["08-20-2023"] = {
        #     "Greg": "Michael McDowell",
        #     "Bob": "Chris Buescher",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["08-26-2023"] = {
        #     "Greg": "Chase Briscoe",
        #     "Bob": "Ryan Preece",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["09-03-2023"] = {
        #     "Greg": "Ricky Stenhouse Jr.",
        #     "Bob": "Michael McDowell",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["09-10-2023"] = {
        #     "Greg": "Austin Dillon",
        #     "Bob": "Tyler Reddick",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["09-16-2023"] = {
        #     "Greg": "Brad Keselowski",
        #     "Bob": "Corey LaJoie",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["09-24-2023"] = {
        #     "Greg": "Bubba Wallace",
        #     "Bob": "Erik Jones",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["10-01-2023"] = {
        #     "Greg": "Riley Herbst",
        #     "Bob": "Brad Keselowski",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["10-08-2023"] = {
        #     "Greg": "Daniel Suarez",
        #     "Bob": "Ty Gibbs",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["10-15-2023"] = {
        #     "Greg": "Justin Haley",
        #     "Bob": "Carson Hocevar",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["10-22-2023"] = {
        #     "Greg": "Alex Bowman",
        #     "Bob": "Austin Dillon",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["10-29-2023"] = {
        #     "Greg": "Ryan Preece",
        #     "Bob": "Chase Briscoe",
        #     "badge_color": "bg-success text-light",
        # }
        # self.individual_bets["11-05-2023"] = {
        #     "Greg": "Chris Buescher",
        #     "Bob": "Denny Hamlin",
        #     "badge_color": "bg-success text-light",
        # }

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet indate_formation for Greg and Bob
            first pick starts at the first of the year and alternates each week
        """
        first_pick = 0
        for x in self.individual_bets:
            if first_pick % 2:
                self.individual_bets[x]["first_pick"] = "Greg"
            else:
                self.individual_bets[x]["first_pick"] = "Bob"
            first_pick += 1
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
