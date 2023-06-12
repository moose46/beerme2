__author__ = "Robert W. Curtiss"
__project__ = "flask-by-example"
# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# summary.py was created on March 31 2021 @ 6:39 PM
# Project: PythonGoogleWeb
import logging


class Summary(object):
    def __init__(self, list_of_individual_bets):
        """

        :type list_of_individual_bets: BeerBet
        """
        self.list_of_individual_bets = list_of_individual_bets
        total_bob_beers = sum(
            x.the_winner()["Bob"] for x in self.list_of_individual_bets
        )
        total_greg_beers = sum(
            x.the_winner()["Greg"] for x in self.list_of_individual_bets
        )
        for x in self.list_of_individual_bets:
            logging.info(f"greg beers = '{x.the_winner()['Greg']}")
        if total_greg_beers > total_bob_beers:
            gregs_cooler = total_greg_beers - total_bob_beers
            bobs_cooler = 0
        else:
            bobs_cooler = total_bob_beers - total_greg_beers
            gregs_cooler = 0
        self.total_beers_owed = {"Bob": bobs_cooler, "Greg": gregs_cooler}

    def __repr__(self) -> str:
        return f"Summary() = \n{self.list_of_individual_bets}\n{self.total_beers_owed}"
