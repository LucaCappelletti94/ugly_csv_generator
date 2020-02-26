import pandas as pd
from random import Random


def random_space(state: Random):
    k = state.randint(1, 10)
    return "".join(state.choices([" ", "\n", "\n\r"], [0.8, 0.15, 0.05], k=k))


def add_random_spaces(csv: pd.DataFrame, state: Random) -> pd.DataFrame:
    return csv.applymap(lambda x: "{s1}{x}{s2}".format(
        s1=random_space(state),
        x=str(x).replace(" ", random_space(state)),
        s2=random_space(state)
    ) if not pd.isna(x) else x)
