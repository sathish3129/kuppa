# https://repl.it/repls/AfraidScratchyWrapper

# Load sample file 
import pandas as pd 


df = pd.read_csv('sample.csv', sep='|', index_col="POLICY")

# print(df[df['ETL_TRANSACTION_DS'].str.upper() == 'ENDORSEMENT'])

group_df =  df.groupby('POLICY')
print(group_df)
