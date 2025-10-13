import csv
import logging
import os
from collections import  namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime


from betData import BetData

DATE_FORMAT = "%m-%d-%Y"
file_path = Path.home() / "beerme" / "data"
beerme2_file_path = (
    Path()
    / "Users"
    / "me"
    / "Documents"
    / "VisualCodeSource"
    / "beerme2_db"
    / "commissioner"
    / "scripts"
    / "csv_data"
)

log_file = Path.cwd() / "files_log.txt"
if not file_path.exists():
    file_path = Path.cwd() / "data"
    log_file = Path.cwd() / "files_log.txt"
    if not file_path.exists():
        print(f"{file_path} Does Not Exist!")
        exit()


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)
DriverBet = namedtuple("DriverBet", "date, person_name, driver_name, badge_color")


class ProcessDataFiles:
    """_summary_Reads data/*.csv files for the results of all races in the data directory
    creates a list of individual race results, but no correlation between two races,except race date
    """

    def __init__(self):

        print(f"Data file_path={file_path}")
        # a list of all race results
        self.race_schedule_results = []
        # print(self.individual_bets)
        # creates a class that reads the races results data files
        self.data = BetData()
        self.individual_bets = self.data.get_bets
        # print(f"{self.individual_bets}")

    # @property
    def bets(self):
        """Return a list of dictionaries of all the bets for Bob and Greg"""
        return self.individual_bets

    def read_data_files(self):  # sourcery skip: low-code-quality
        # print("In read_data_files")
        # find all the results for all the races in the data directory that match the 02-02-2023.csv pattern
        for bet in self.data.individual_bets:
            # get the track name from the bet data
            # print(f"bet={bet}")
            race_track = self.individual_bets[bet]["Track"]
            race_date = bet
            # Changed name to .csv files
            results_file_name = f"*{bet}*.csv"

            print(f"1. Processing {race_track}  - {results_file_name}")
            found = False
            # check to see if the race results file exists (example: 08-10-2025.csv)
            for _ in file_path.glob(results_file_name):
                found = True
            # if the race results file does not exist, create an empty file (example: 08-10-2025.csv)
            if not found:
                print(f"Checking -> {results_file_name}")
                if not os.path.isfile(Path(f"{file_path}/{race_date}.csv")):
                    print(f"Does Not exist -> {race_date}.csv")
                    exit()
                    # with open(Path(f"{f.parent}/{race_date}.csv"), "w") as file:
                    #     pass
            for f in file_path.glob(results_file_name):
                # print(f.stem,f.suffix)
                print(f"2. Processing {race_track} - {race_date} - {f.parent}/{f.name}")
                with open(Path(f"{f.parent}/{f.name}"), "r") as file:
                    reader = csv.reader(file, delimiter="\t")
                    try:
                        # csv file must have header, could be empty or no data
                        # create a named tuple with the header names
                        rawResult = namedtuple("rawResult", next(reader), rename=True)
                    except Exception as e:
                        print(f"Error reading {f.name}: {e}")
                        exit()
                    # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])
                    # print(f"open ok {f.name}")
                    for row in reader:
                        # try:
                        result = rawResult(
                            *row
                        )  # unpack csv data row into the named tuple
                        # except Exception as e:
                        #     print(f.name)
                        # logging.info(f"raw result: {result}")
                        # if the date is in 2024
                        if strptime(race_date, DATE_FORMAT) > strptime(
                            "01-01-2024", DATE_FORMAT
                        ):
                            # print(f"{bet}")
                            # logging.info(f"date {race_date} is > 01-01-2024")
                            # loop through the bets and check for a driver in the results, if found add to the results list
                            for name in self.individual_bets[
                                race_date
                            ]:  # get the bet data for the this race data
                                # the key [race_date][name] returns the driver name
                                # print(f"name in individual_bets: {race_date} {name}")
                                if (
                                    self.individual_bets[race_date][name]
                                    == result.DRIVER
                                ):
                                    # print(f"{race_date} .... {result.DRIVER}")
                                    parts = race_track.split(
                                        " "
                                    )  # look to see if the filename has spaces in it
                                    capitalized_parts = [
                                        p.capitalize() for p in parts
                                    ]  # cap first letter(s) of name
                                    # add results of the race and the bet data for this player to the list of results
                                    driver_last_name = result.DRIVER.split(" ")
                                    # martin truex jr., del jr.
                                    if (
                                        len(driver_last_name) > 2
                                        and driver_last_name[2] == "Jr."
                                    ):
                                        del driver_last_name[2]
                                        # print(driver_last_name)
                                    self.race_schedule_results.append(
                                        {
                                            "race_date": race_date,
                                            "race_track": " ".join(
                                                [
                                                    word.capitalize()
                                                    for word in race_track.split(" ")
                                                ]
                                            ),
                                            "driver_name": f'{result.DRIVER.split(" ")[len(driver_last_name)-1][:8]} {result.POS}',  # get the last name and trunc it to 8 chars
                                            "finish": int(result.POS),
                                            "player_name": name,
                                            "beers": 1 if int(result.POS) == 0 else 0,
                                            "car_number": result.CAR,
                                            "badge_color": self.individual_bets[
                                                race_date
                                            ]["badge_color"],
                                        }
                                    )
                                    # logging.info(f"line 170 = {result}")
                                    # print(result)
        # for b in self.race_schedule_results:
        #     logging.info(f"files.py race_schedule_results ={b}")
        return sorted(
            self.race_schedule_results,
            key=itemgetter("race_date", "player_name"),
        )
        # return sorted_race_results


if __name__ == "__main__":
    print(f"Debugging {__file__} .........")
    p = ProcessDataFiles()
    print(f"ProcessDataFiles: {type(p)}")
    race_results_data = p.read_data_files()
    for x in race_results_data:
        logging.debug(f"files.py->race_results->{x}")
        print(x)
