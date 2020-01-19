"""
Utilities for use with pandas.DataFrame
"""

import pandas as pd


def summary(data=None, groups=None, column=None, *args):
    """
    Create a table of descriptive statistics of the underlying data. Function will calculate
    the percentiles in `args` in addition to the min, max, mean, std, and count. `summary` is
    similar to `pandas.describe` but works with grouped data and populates the data in columns
    rather than rows

    :param data: DataFrame of data
    :param groups: columns to group by
    :param column: column to calculate
    :param args: percentiles to apply
    :return: DataFrame
    """
    if data is None or column is None:
        return data

    df = data[groups].drop_duplicates()
    df.set_index(groups, inplace=True)

    df["count"] = data.groupby(groups)[column].count()
    df["min"] = data.groupby(groups)[column].min()
    df["mean"] = data.groupby(groups)[column].mean()
    df["max"] = data.groupby(groups)[column].max()
    df["std"] = data.groupby(groups)[column].std()

    for p in args:
        try:
            p = float(p)
        except ValueError:
            next

        col = "p" + str(p)
        df[col] = data.groupby(groups)[column].quantile(p)

    return df

