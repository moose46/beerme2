from collections import defaultdict


class MyWager:
    def __init__(self):
        self.gregs_bet = defaultdict()
        self.bobs_bet = defaultdict()
        self.bobs_total = 0  # total beers won from greg
        self.gregs_total = 0  # total beers won from bob

    def reset(self):
        self.bobs_bet = defaultdict()
        self.gregs_bet = defaultdict()

    def bob(self, race_results):
        self.bobs_bet = race_results
        self.beers = self.bobs_bet["beers"]
        # self.driver = self.bobs_bet["driver_name"]
        # self.bobs_total += self.bobs_bet["beers"]

    def greg(self, race_results):
        self.gregs_bet = race_results
        self.gregs_total += self.gregs_bet["beers"]

    def enabled(self):
        return bool(self.gregs_bet and self.bobs_bet)

    def brew_some_beer(self):
        if (
            self.bobs_bet["finish"] < self.gregs_bet["finish"]
        ):  # bob finished ahead of greg
            self.bobs_bet["beers"] = 2 if self.bobs_bet["finish"] == 1 else 1
        if (
            self.bobs_bet["finish"] > self.gregs_bet["finish"]
        ):  # greg finished ahead of bob
            self.gregs_bet["beers"] = 2 if self.gregs_bet["finish"] == 1 else 1
