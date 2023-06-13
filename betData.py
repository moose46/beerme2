# betting data goes here
from collections import defaultdict
from datetime import date

# import the datetime module
import datetime

# datetime in string format for may 25 1999
input = "2021/05/25"

# format
# format = '%Y/%m/%d'
format = "%m-%d-%Y"
# convert from string format to datetime format

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

    @property
    def get_bets(self):
        """_summary_

        Returns:
            Returns a list of dictionaries of all the current bet information for Greg and Bob
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
        self.race_date = datetime.datetime.strptime(race_date, format)

        self.track = track
        self.player = player
        self.driver = driver
        self.finish = -1
        self.badge_color = badge_color

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
        return f"{self.race_date}"


def create_bets():
    bets = []
    bets.append(
        Bet(race_date="02-19-2023", track="Daytona", player="Bob", driver="Ryan Blaney")
    )
    bets.append(
        Bet(
            race_date="02-19-2023", track="Daytona", player="Greg", driver="Kyle Larson"
        )
    )
    bets.append(
        Bet(
            race_date="02-26-2023",
            track="california",
            player="Greg",
            driver="Ryan Blaney",
        )
    bets.append(
        Bet(
            race_date="02-26-2023",
            track="california",
            player="Bob",
            driver="Joey Logano",
        )
    )
    return bets


if __name__ == "__main__":
    bets = create_bets()
    bets = sorted(bets)
    print(type(bets))
    for bet in bets:
        print(bet)
