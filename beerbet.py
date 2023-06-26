__author__ = "Robert W. Curtiss"
__project__ = "flask-by-example"

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# beerbet.py was created on March 31 2021 @ 6:34 PM
# Project: PythonGoogleWeb
import logging

from entry import Entry


class BeerBet(Entry):
    bob: Entry
    greg: Entry

    def __init__(self, bob, greg, race_name, badge_color):
        self.race_name = race_name
        self.bob = bob
        self.greg = greg
        self.race_name = race_name
        self.badge_color = badge_color

    def the_winner(self):
        # if self.greg.finish > self.bob.finish:
        self.bob.beer = self.bob.beers  # type: ignore
        # elif self.greg.finish < self.bob.finish:
        self.greg.beer = self.greg.beers  # type: ignore

        return {
            "Bob": self.bob.beers,
            "Greg": self.greg.beers,
            "badge_color": self.badge_color,
        }

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            f"Race: {self.race_name}:\n"
            f"\tName: Driver:{self.bob.driver_name} Finish:{self.bob.finish} Beers:{self.bob.beers} color:{self.badge_color}\n"
            f"\tName: Driver:{self.greg.driver_name} Finish:{self.greg.finish} Beers:{self.greg.beers} color:{self.badge_color}"
        )
