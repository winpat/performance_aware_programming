from math import radians, sin, cos, sqrt, asin
import time
import json


EARTH_RADIUS_KM = 6371


def haversine_distance(x0, y0, x1, y1, r):
    """Compute haversine distance."""

    dy = radians(y1 - y0)
    dx = radians(x1 - x0)
    y0 = radians(y0)
    y1 = radians(y1)

    root_term = (sin(dy / 2) ** 2) + cos(y0) * cos(y1) * (sin(dx / 2) ** 2)
    return 2 * r * asin(sqrt(root_term))


def main(data):
    result = sum(
        haversine_distance(
            pair["x0"], pair["y0"], pair["x1"], pair["y1"], EARTH_RADIUS_KM
        )
        for pair in data["pairs"]
    )
    return result / len(data["pairs"])
