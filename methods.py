import pandas as pd
import numpy as np

# expanding terminal window to display the df
desired_width = 320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 15)

df = pd.read_csv(r'C:\Users\SystemAdmin\Desktop\statsgg\gamedata\aggregate_gm_data.csv')

df['KDA'] = (df['kills'] + df['assists']) / df['deaths']

# incase of perfect KDA
df.loc[df['KDA'] == float('inf'), 'KDA'] = (df['kills'] + df['assists']) / 1

# champions sorted by winrate
new_df = df.groupby('championName').mean().sort_values('win', ascending=False)
# print(new_df.head(40))

# Most Popular Picks
df['count'] = 1
picks_df = df.groupby('championName').count()['count']
# print(picks_df.head(40))
# divide the pick count by (total games / 10) to find the pickrate of a champion (10 champion entries per game)

# Most popular summoner spells on each champion
spells_df = df.groupby(['spell1', 'spell2']).count()['count']
# print(spells_df)
# if spell1 is x, how many are spell2 (can resolve the flash on 'd' vs 'f' debate)
# group by spell1 or spell2 to get actual count values

# Get most popular summoner spells on each champion
summoner_spells_df = df.groupby(['championName', 'spell1', 'spell2']).count()['count']
# print(summoner_spells_df.head(30)) OR you can also groupby just spell1 and spell2 for cleaner counts

# Match stats: Pull up the average for that champion Row and compare winrate, kills, deaths, assists (NOT JUST KDA), etc.

# TRIVIA: Which Champions Die the Most, Kills, Gold, CS, etc.
trivia_df = df.groupby('championName').mean().sort_values('deaths', ascending=False)
# print(trivia_df)

# Cross-referencing champions
# chunked_df = pd.read_csv(r'C:\Users\SystemAdmin\Desktop\statsgg\gamedata\aggregate_gm_data.csv', chunksize=10)
# for df in chunked_df:



