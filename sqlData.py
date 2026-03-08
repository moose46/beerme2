import csv
import os
import sqlite3
from pathlib import Path

from betData import BetData

DATE_FORMAT = "%m-%d-%Y"

RESULTS_TABLE = """
create table results (
race_date text,
driver char[32],
finish integer default 0)
"""

BETS_TABLE = """
create table bets (
track char[32],
race_date text,
greg char[32],
greg_finish integer default 0,
bob char[32],
bob_finish integer default 0,
badge_color char[32]
)
"""
TRACK = 0
RACE_DATE = 1
GREG = 2
GREG_FINISH = 3
BOB = 4
BOB_FINISH = 5
BADGE_COLOR = 6

file_path = Path.home() / "beerme" / "data"
log_file = Path.cwd() / "files_log.txt"
if not file_path.exists():
    file_path = Path.cwd() / "data"
    log_file = Path.cwd() / "files_log.txt"
    if not file_path.exists():
        print(f"{file_path} Does Not Exist!")
        exit()


class SQLRaceData:
    def __init__(self):
        self.conn = None

        try:
            self.conn = sqlite3.connect(":memory:")
        except Exception as e:
            print(e)
            exit()
        print("Database Connected")
        self.cur = self.conn.cursor()
        self.create_tables()
        self.data = BetData()
        self.individual_bets = self.data.get_bets
        self.insert_bets(self.individual_bets)
        self.read_nascar_csv()

    def create_tables(self):
        self.cur.execute(RESULTS_TABLE)
        self.conn.commit()
        self.cur.execute(BETS_TABLE)
        print("Tables Created")

    def insert_bets(self, bet_data):
        for bet in bet_data:
            self.cur.execute(
                "insert into bets (race_date, greg, bob, track, badge_color) values (?, ?, ?, ?, ?)",
                (
                    bet,
                    bet_data.get(bet)["Greg"],
                    bet_data.get(bet)["Bob"],
                    bet_data.get(bet)["Track"],
                    bet_data.get(bet)["badge_color"],
                ),
            )

    def insert_results(self, race_date, driver, finish):
        try:
            self.cur.execute(
                "insert into results (race_date, driver, finish) values (?, ?, ?)",
                (
                    race_date,
                    driver,
                    finish,
                ),
            )
        except Exception as e:
            print(e)
            return
        print("Results Inserted")

    def get_results(self):
        self.cur.execute("select * from results")
        return self.cur.fetchall()

    def read_nascar_csv(self):
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
                with open(Path(f"{f.parent}\\{f.name}"), "r") as file:
                    reader = csv.DictReader(file, delimiter="\t")
                    try:
                        # csv file must have header, could be empty or no data
                        # create a named tuple with the header names
                        print(f"3. Processing {race_date}")
                        # data_dict = list(reader)
                        for row in reader:
                            print(f"4. Processing {row}")
                            self.insert_results(race_date, row["DRIVER"], row["POS"])

                    except Exception as e:
                        print(f"Error reading {f.name}: {e}")
                        exit()


if __name__ == "__main__":
    db = SQLRaceData()
    print(db.get_results())
