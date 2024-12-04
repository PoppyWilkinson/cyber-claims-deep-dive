import pandas as pd

# Temp import to use whilst testing
df = pd.read_csv('test_output.csv')

"""
For claims data:
- Industry blanks to be insurance
- Tidy up industry categories 
- Policy YOA to be 2010 onwards (filter this in SQL query)
- Think about which dates will be used and whether they need datetime formatting (keep inception, remove expiry)
- How would you handle lead/follow blanks -> remove as there is only a few? or use leader col to assume follow?
- Think about removing risk code, renewal type, leader, sub class, cat code, claim close date, policy group
- Choose between signed and written line (remove written)
- Big clean up on loss location/city/state columns, also merge three into one (perhaps spend less time and mention as
    future improvement in report)
- What to do with 84 loss date blanks -> use claim open date?
- Lots of 0 incurred, may have to remove this column

For policy data:
- Lead/follow, industry name, rfid blanks
- Insured name cleaning
- Convert count nulls to 0s
- Bandings for numerical cols -> GGWP, signed line, counts
- Use YOA for clustering and remove other dates until time series analysis needed
"""


def clean_data_extract(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df
    return clean_df