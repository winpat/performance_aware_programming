from random import uniform
import json
from sys import argv


DATA_FILE = "haversine/data/data.json"


def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)


def random_latitude():
    return uniform(-0.9, 0.9) * 100


def random_longitude():
    return uniform(-0.18, 0.18) * 1000


def generate_haversine_data(num_points):
    data = {
        "pairs": [
            {
                "x0": random_longitude(),
                "y0": random_latitude(),
                "x1": random_longitude(),
                "y1": random_latitude(),
            }
            for _ in range(num_points)
        ]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    generate_haversine_data(int(argv[1]))
