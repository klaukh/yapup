"""
Utilities for general use
"""

import pandas as pd
import random


def cartesianproduct(*args):
    """Create full cartesian product of all objects passed"""

    # Create a random string to name a new random column for merging
    key_col = randomstring(16)
    out = pd.DataFrame(args[0].drop_duplicates())
    out[key_col] = 1

    for itm in args[1:]:
        itm = pd.DataFrame(itm.drop_duplicates())
        itm[key_col] = 1
        out = out.merge(itm, on=key_col)

    out.drop(columns=key_col, inplace=True)
    return out

