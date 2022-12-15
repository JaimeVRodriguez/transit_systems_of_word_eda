import numpy as np
import pandas as pd


def read_file(csv_file):

    df = pd.read_csv(csv_file)
    return df


if __name__ == "__main__":

    cities = read_file("data/cities.csv")
    print(cities)
