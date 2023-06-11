from pathlib import Path
from ..files import ProcessDataFiles
from os.path import exists, isfile
import os
import re
import pytest


cwd = os.getcwd()

data_directory = Path("C://Users//me//Documents//VisualCodeSource//beerme2//data")
root_directory = Path.home() / "documents" / "VisualCodeSource" / "beerme2"


@pytest.fixture
def process_data_files():
    return ProcessDataFiles()


def test_bet_count(process_data_files):
    # pdf = ProcessDataFiles()
    assert process_data_files.bets() != None
    assert len(process_data_files.bets()) == 12  # 05-07-2023 last race


def test_race_date(process_data_files):
    print(f'\n **** {process_data_files.individual_bets["03-26-2023"]} \n')
    print(f" =================== {len(process_data_files.individual_bets)}")
    assert process_data_files.individual_bets["03-26-2023"] != []


def test_data_file(process_data_files):
    """Test sure data file exists for each date bet"""
    for b in process_data_files.individual_bets:
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
        # assert found == True
