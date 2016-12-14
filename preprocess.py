import pandas as pd
from datetime import timedelta

def preprocess(self, data):
    data.drop('ASS_ASSIGNMENT', 1, inplace=True, errors='ignore')
    data.set_index('DATE', inplace=True)
    data.sort_index(0, inplace=True)
    data.reset_index(inplace=True)

    dates_to_be_added = []
    d2 = data.loc[0].DATE

    for i, row in data[1:].iterrows():
        d1 = row.DATE
        e = int((d1-d2).total_seconds())
        if not e == 1800:
            for k in range(int(e / 1800) - 1):
                dates_to_be_added.append(d2 + timedelta(seconds=(1800*(k+1))))
        d2 = d1

    nndf = pd.DataFrame(list(map(lambda d: [d, None], dates_to_be_added)), columns=['DATE', 'CSPL_RECEIVED_CALLS'])

    data = data.append(nndf, ignore_index=True)

    data.set_index('DATE', inplace=True)
    data.sort_index(0, inplace=True)
    data.reset_index(inplace=True)

    return data
