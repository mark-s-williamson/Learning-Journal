import pandas as pd
import numpy as np

df = pd.read_csv('spreadspoke_scores.csv')
#print (df.loc[0, 'team_home'])

filtered_df = df[(df['team_home'] == 'Miami Dolphins')]
print(filtered_df)

summary_stats = df.describe()
print(summary_stats)

filtered_summary_stats = filtered_df.describe()
print(filtered_summary_stats)
