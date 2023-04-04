from pathlib import Path
from ..files import individual_bets
from os.path import exists, isfile
import os
import re


cwd = os.getcwd()

data_directory = Path("C://Users//me//Documents//VisualCodeSource//beerme2//data")
root_directory = Path.home() / "documents" / "VisualCodeSource" / "beerme2"


def test_bet_count():
    assert individual_bets != None
    assert len(individual_bets) == 6


def test_race_date():
    print(f'\n **** {individual_bets["03-26-2023"]} \n')
    print(f" =================== {len(individual_bets)}")
    assert individual_bets["03-26-2023"] != []


def test_data_file():
    """Test sure data file exists for each date bet"""
    for b in individual_bets:
        """Returns date strings: 03/12/2023"""
        file_name = f".*results.*_{b}_.txt"
        # pattern = re.compile("{b}")
        # print(pattern)
        found = False
        print(f"============= {b} file_name = {file_name}")
        for f in data_directory.glob(f"results*_{b}_.txt"):
            # print(f"{f}")
            # print(re.search(file_name, str(f)))
            found = True
            assert f.is_file()
        assert found == True
