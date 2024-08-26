import csv
import logging
import re
from collections import defaultdict, namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime

from betData import BetData

DATE_FORMAT = "%m-%d-%Y"
file_path = Path.home() / "beerme" / "data"
log_file = Path.cwd() / "logs" / "files_log.txt"
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
    """_summary_Reads data/results* txt files for the results of all races in the data directory
    creates a list of individual race results, but no correlation between two races,except race date
    """

    def __init__(self):

        print(f"Data file_path={file_path}")
        # a list of all race results
        self.race_schedule_results = []
        # print(self.individual_bets)
        # creates a class that reads the races results data files
        data = BetData()
        self.individual_bets = data.get_bets
        # print(f"{self.individual_bets}")

    # @property
    def bets(self):
        """Return a list of dictionaries of all the bets for Bob and Greg"""
        return self.individual_bets

    def read_data_files(self):  # sourcery skip: low-code-quality
        # print("In read_data_files")
        # find all the results for all the races in the data directory that match the results*2023_.txt pattern
        for f in file_path.glob("results*2024_.txt"):
            race_track = f.stem.split("_")[1]
            race_date = re.findall(r"\d+-\d+-\d+", f.name)[
                0
            ]  # get the date from the file name
            print(f"Processing {race_track.capitalize()} - {race_date}")
            # read each file
            with open(Path(f"{f.parent}/{f.name}"), "r") as file:
                reader = csv.reader(file, delimiter="\t")
                # csv file must have header
                rawResult = namedtuple("rawResult", next(reader), rename=True)
                # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])
                # print(f.name)
                for row in reader:
                    # try:
                    result = rawResult(*row)  # unpack csv data row into the named tuple
                    # except Exception as e:
                    #     print(f.name)
                    logging.info(f"raw result: {result}")
                    if strptime(race_date, DATE_FORMAT) > strptime(
                        "01-01-2024", DATE_FORMAT
                    ):
                        # logging.info(f"date {race_date} is > 01-01-2024")
                        # loop through the bets and check for a driver in the results, if found add to the results list
                        for name in self.individual_bets[
                            race_date
                        ]:  # get the bet data for the this race data
                            # the key [race_date][name] returns the driver name
                            logging.info(f"name in individual_bets: {name}")
                            if self.individual_bets[race_date][name] == result.DRIVER:
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
                                        "badge_color": self.individual_bets[race_date][
                                            "badge_color"
                                        ],
                                    }
                                )
                                # logging.info(f"line 170 = {result}")
                                # print(result)

        for b in self.race_schedule_results:
            logging.info(f"files.py race_schedule_results ={b}")
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
