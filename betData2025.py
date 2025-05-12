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

        self.individual_bets["03-23-2025"] = {
            "Greg": "Josh Berry",
            "Bob": "William Byron",
            "Track": "Miami",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["03-30-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Chase Elliott",
            "Track": "Martinsville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-06-2025"] = {
            "Greg": "Denny Hamlin",
            "Bob": "William Byron",
            "Track": "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-13-2025"] = {
            "Greg": "Christopher Bell",
            "Bob": "Kyle Larson",
            "Track": "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["04-27-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "Track": "Talladega",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-04-2025"] = {
            "Greg": "William Byron",
            "Bob": "Kyle Larson",
            "Track": "Texas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["05-11-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Christopher Bell",
            "Track": "Kansas",
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
