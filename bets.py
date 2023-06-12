__author__ = "Robert W. Curtiss"
__project__ = "flask-by-example"

# https://www.youtube.com/watch?v=1aHNs1aEATg&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=7
# Author: Robert W. Curtiss
# bets.py was created on April 15 2021 @ 3:01 PM
# Project: nascar
import logging
import operator
from itertools import groupby
from operator import itemgetter

from beerbet import BeerBet
from entry import Entry
from files import ProcessDataFiles
from summary import Summary
from wager import MyWager

logging.basicConfig(
    filename="bets_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

# read all results*.txt files for 2023 and the drivers finish position
# for bets that greg and bob placed
p = ProcessDataFiles()
race_results = p.read_data_files()
individual_race_results = list(race_results)

# team_race_results = list(filter(lambda results: results["team_bet"], race_results))
list_of_individual_bets = []

wager = MyWager()
# go through the raw results list and sort out team from individual bets
for date, items in groupby(individual_race_results, key=itemgetter("race_date")):
    wager.reset()  # zero out one bet
    for player in items:
        # create either bob or gregs bet in the wager
        operator.methodcaller(player["player_name"].lower(), player)(wager)
        # if both bets have been placed create a beer bet
        if wager.enabled():
            wager.brew_some_beer()
            # list_of_individual_bets.append(wager)
            list_of_individual_bets.append(
                BeerBet(
                    race_name=wager.bobs_bet["race_track"],
                    greg=Entry(
                        driver_name=wager.gregs_bet["driver_name"],
                        finish=wager.gregs_bet["finish"],
                        player_name=wager.gregs_bet["player_name"],
                        beers=wager.gregs_bet["beers"],
                        car_number=wager.gregs_bet["car_number"],
                        badge_color=player["badge_color"],
                    ),
                    bob=Entry(
                        driver_name=wager.bobs_bet["driver_name"],
                        finish=wager.bobs_bet["finish"],
                        player_name=wager.bobs_bet["player_name"],
                        beers=wager.bobs_bet["beers"],
                        car_number=wager.bobs_bet["car_number"],
                        badge_color=player["badge_color"],
                    ),
                    badge_color=player["badge_color"],
                )
            )

# beers count has already been scored
# for l in list_of_individual_bets:
#     logging.info(f"bets.py->list_of_individul_bets {l}")
betting_summary = Summary(list_of_individual_bets)
