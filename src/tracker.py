import json
from datetime import date

DATA_FILE = "src/data.json"


def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_today():
    return str(date.today())