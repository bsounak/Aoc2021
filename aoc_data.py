import os

cache = os.path.join(os.path.expanduser("~"), ".aoc2021")


def load(day: int) -> list:
    fname = "day" + str(int(day)) + ".txt"
    if not os.path.isfile(os.path.join(cache, fname)):
        raise Exception("No data available for day{} at {}".format(day, cache))
    with open(os.path.join(cache, fname), "rb") as f:
        data = f.read()

    return data
