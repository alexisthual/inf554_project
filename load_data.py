import pandas as pd

# Loading training data
# df = pd.read_csv(
#     'domplete_data.txt',
#     sep='\t',
#     usecols=['DATE','CSPL_RECEIVED_CALLS','ASS_ASSIGNMENT'],
#     parse_dates=[0]
# )
#
# df[['CSPL_RECEIVED_CALLS']] = df[['CSPL_RECEIVED_CALLS']].apply(pd.to_numeric)

# Loading submission file
dfsub = pd.read_csv(
    'submission.txt',
    sep='\t',
)
