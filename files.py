import logging
import csv
import re
from collections import defaultdict
from collections import namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime

DATE_FORMAT = "%m-%d-%Y"
file_path = Path.home() / "beerme" / "data"
log_file = Path.home() / "beerme" / "files_log.txt"
if not file_path.exists():
    file_path = Path.cwd() / "data"
    log_file = Path.cwd() / "files_log.txt"


logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)
DriverBet = namedtuple("DriverBet", "date, person_name, driver_name")

individual_bets = defaultdict(list)
# individual_bets.setdefault("missing_key")
individual_bets["02-19-2023"] = {
    "Greg": "Kyle Larson",
    "Bob": "Ryan Blaney",
}
individual_bets["02-26-2023"] = {
    "Greg": "Ryan Blaney",
    "Bob": "Joey Logano",
}
individual_bets["03-05-2023"] = {
    "Greg": "Kyle Larson",
    "Bob": "Kyle Busch",
}
individual_bets["03-12-2023"] = {
    "Greg": "Ryan Blaney",
    "Bob": "William Byron",
}
individual_bets["03-19-2023"] = {
    "Greg": "Kyle Busch",
    "Bob": "Joey Logano",
}
individual_bets["03-26-2023"] = {
    "Greg": "Tyler Reddick",
    "Bob": "Ross Chastain",
}


class ProcessDataFiles:
    def __init__(self) -> None:
        self.race_schedule_results = []

    def read_data_files(self):
        for f in file_path.glob("results*2023_.txt"):
            race_track = f.stem.split("_")[1]

            with open(Path(f"{f.parent}/{f.name}"), "r") as file:
                reader = csv.reader(file, delimiter="\t")
                # csv file must have header
                rawResult = namedtuple("rawResult", next(reader), rename=True)
                # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])
                print(f.name)
                for row in reader:
                    # try:
                    result = rawResult(*row)  # unpack csv data row into the named tuple
                    # except Exception as e:
                    #     print(f.name)

                    race_date = re.findall(r"\d+-\d+-\d+", f.name)[
                        0
                    ]  # get the date from the file name
                    if strptime(race_date, DATE_FORMAT) > strptime(
                        "01-01-2023", DATE_FORMAT
                    ):
                        # loop through the bets and check for a driver in the results, if found add to the results list
                        for name in individual_bets[race_date]:
                            # the key [race_date][name] returns the driver name
                            if individual_bets[race_date][name] == result.DRIVER:
                                parts = race_track.split(
                                    " "
                                )  # look to see if the filename has spaces in it
                                capitalized_parts = [
                                    p.capitalize() for p in parts
                                ]  # cap first letter(s) of name

                                self.race_schedule_results.append(  # add it to the results list
                                    {
                                        "race_date": race_date,
                                        "race_track": " ".join(
                                            [
                                                word.capitalize()
                                                for word in race_track.split(" ")
                                            ]
                                        ),
                                        "driver_name": result.DRIVER,
                                        "finish": int(result.POS),
                                        "player_name": name,
                                        "beers": 0,
                                        "team_bet": False,
                                        "car_number": result.CAR,
                                    }
                                )
                    # logging.info(result)
                    # print(result)

        """
            Only data in the list is either a team bet or individual bet
            , separated by team_bet, either true or false
           sort the list by race_date, team_bet and player name (greg or bob) 
        """
        sorted_race_results = sorted(
            self.race_schedule_results,
            key=itemgetter("race_date", "team_bet", "player_name"),
        )
        for b in sorted_race_results:
            logging.info(b)
        return sorted_race_results


if __name__ == "__main__":
    p = ProcessDataFiles()

    race_results_data = p.read_data_files()
    # print(race_results_data)
