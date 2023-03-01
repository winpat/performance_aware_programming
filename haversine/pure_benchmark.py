from haversine.pure import main
from haversine.data_generator import load_data
import pytest


def benchmark_pure(benchmark):
    data = load_data()
    benchmark(main, data)
