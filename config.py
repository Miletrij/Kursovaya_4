from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE = Path(BASE_DIR, "data", "vacancies_hh.json")
print(FILE)