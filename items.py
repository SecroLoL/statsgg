import json

with open(r'.\raw_data\item.json', 'r') as handle:
    parsed = json.load(handle)
    print(parsed['data'])