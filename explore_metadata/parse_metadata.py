# To use this script you have to install ijson. See https://pypi.python.org/pypi/ijson/
# Usage: python parse_metadata.py
import ijson

# nasa_metadata2.json is the file downloaded from https://data.nasa.gov/data.json
filename='nasa_metadata2.json'
f = open(filename, 'rb')

# nasa_metadata2.json is the file downloaded from https://data.nasa.gov/data.json
objects = ijson.items(f, 'dataset');
count = 0
summary = []

# grab only title and description 
for obj in objects:
    for dataset in obj:
        summary.append({"title":dataset["title"
            ],"description":dataset["description"]});
    count = count + 1
    if count > 5:
        break

# write title and description to new json file
import json
with open('nasa_text2.json', 'w') as outfile:
    json.dump(summary, outfile)
