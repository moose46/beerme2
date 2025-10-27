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
        self.individual_bets["05-25-2025"] = {
            "Greg": "Christopher Bell",
            "Bob": "William Byron",
            "Track": "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-01-2025"] = {
            "Greg": "Denny Hamlin",
            "Bob": "Ross Chastain",
            "Track": "Nashville",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-08-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Michigan",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-15-2025"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Ross Chastain",
            "Track": "Mexico",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-22-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Pocono",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["06-28-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Joey Logano",
            "Track": "Atlanta",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-06-2025"] = {
            "Greg": "Tyler Reddick",
            "Bob": "Shane van Gisbergen",
            "Track": "Chicago",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-13-2025"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "AJ Allmendinger",
            "Track": "Sonoma",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-20-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Dover",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["07-27-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "William Byron",
            "Track": "Indy",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-03-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "Track": "Iowa",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-10-2025"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Chris Buescher",
            "Track": "Watkins Glenn",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-16-2025"] = {
            "Greg": "Christopher Bell",
            "Bob": "Denny Hamlin",
            "Track": "Richmand",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-23-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Alex Bowman",
            "Track": "Daytona",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["08-31-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "Track": "Darlington",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-07-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Denny Hamlin",
            "Track": "St. Louis",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-13-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Kyle Larson",
            "Track": "Bristol",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-21-2025"] = {
            "Greg": "Christopher Bell",
            "Bob": "Ryan Blaney",
            "Track": "New Hampshire",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["09-28-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Kansas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-05-2025"] = {
            "Greg": "Shane van Gisbergen",
            "Bob": "Kyle Larson",
            "Track": "Charlotte",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-12-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "Denny Hamlin",
            "Track": "Las Vegas",
            "badge_color": "bg-warning text-dark",
        }
        self.individual_bets["10-19-2025"] = {
            "Greg": "Ryan Blaney",
            "Bob": "William Byron",
            "Track": "Talladega",
            "badge_color": "bg-warning text-dark",
        }

        self.individual_bets["10-26-2025"] = {
            "Greg": "Kyle Larson",
            "Bob": "Denny Hamlin",
            "Track": "Martinsville",
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
