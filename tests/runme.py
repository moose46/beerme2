import os
from pathlib import Path

print(os.getcwd())

file_path = Path.cwd() / "beerme" / "data" / "results_cota_03-26-2023_.txt"
file_path = Path.home()

print(file_path)

print(file_path.is_file())
