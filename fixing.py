import pandas as pd

paths = ['raw_data/EUW data/aggregated_euw_data.csv', 'raw_data/gm data/aggregate_gm_data.csv', 'raw_data/Korean Chall/aggregated_kr_chally_data.csv', 'raw_data/aggregated_br_data.csv']

df = pd.read_csv(paths[0])
for path in paths[1:]:
    temp = pd.read_csv(path)
    print(temp)
    df = pd.concat([df, temp], ignore_index=True)
    
df.to_csv('./raw_data/aggregated_match_data.csv')

