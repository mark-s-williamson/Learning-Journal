import pandas as pd
import numpy as np

df = pd.read_csv('spreadspoke_scores.csv')
sorted_data = df.sort_values('score_home')
#print (sorted_data)
grouped_data = df.groupby(['team_home', 'team_away'])
aggregated_data = grouped_data['score_home'].mean()

print (aggregated_data)