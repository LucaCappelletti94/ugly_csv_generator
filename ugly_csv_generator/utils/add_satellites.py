import pandas as pd
import os
from random import Random
from glob import glob
from .add_chunk import add_chunk

def random_satellite(state: Random):
    satellites = glob("{}/satellites/*.csv".format(os.path.dirname(os.path.abspath(__file__))))
    return pd.read_csv(state.choice(satellites))


def add_satellites(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    if state.randint(0, 1) == 1:
        csv = add_chunk(csv, random_satellite(state), 0)
    if state.randint(0, 1) == 1:
        csv = add_chunk(csv, random_satellite(state), len(csv))
    return csv