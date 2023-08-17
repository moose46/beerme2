import csv
import re
from collections import defaultdict, namedtuple
from datetime import date
from pathlib import Path
from string import capwords


class Races:
    def __init__(self, year: str) -> None:
        self.year = year
        self.file_path = Path.cwd() / "data"
        self.races = {}
        self.drivers = {}
        # create a dictionay of all race for the year passed
        for f in self.file_path.glob(f"results*{self.year}_.txt"):
            race_track = f.stem.split("_")[1]
            race_date = re.findall(r"\d+-\d+-\d+", f.name)[
                0
            ]  # get the date from the file name
            # print(f"Processing {race_track.capitalize()} - {race_date}")
            self.races[race_date] = {"track": capwords(race_track), "file_name": f}

    def get_all_race_dates(self) -> dict:
        # year: 2023
        return self.races

    def get_all_drivers(self):
        for f in sorted(self.races.keys()):
            with open(self.races[f]["file_name"]) as file:
                reader = csv.reader(file, delimiter="\t")
                rawResult = namedtuple("rawResult", next(reader), rename=True)
                for row in reader:
                    result = rawResult(*row)  # unpack csv data row into the named tuple
                    self.drivers[result.DRIVER] = {
                        "car": result.CAR,
                        "race_results": {},
                    }
            # open(race_results_file,'+r')
        return self.drivers


x = Races("2023")
x.get_all_drivers()
# print(z)
