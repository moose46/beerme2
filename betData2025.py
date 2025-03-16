from collections import defaultdict, namedtuple

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
        self.individual_bets["02-23-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Austin Cindric",
            "Track": "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-02-2025"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Tyler Reddick",
            "Track": "COTA",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-09-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Christopher Bell",
            "Track": "Phoenix",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-16-2025"] = {
            "Greg": "Christopher Bell",
            "Bob": "Kyle Larson",
            "Track": "Las Vegas",
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
