def write_property(data_objects, prop_name):
    import json
    count = 0
    summary = []
     # grab only id and specified property 
    for obj in data_objects:
        for dataset in obj:
            summary.append({ \
                "id": dataset["_id"]["$oid"], \
                 prop_name:dataset.get(prop_name, '') \
                 })          
        count = count + 1
        if count > 5:
            break

    # write title and description to new json file
    outfile = open('nasa_' + prop_name + '.json', 'w')
    json.dump(summary, outfile)


def parse_metadata(prop_name):
    # To use this script you have to install ijson. See https://pypi.python.org/pypi/ijson/
    # Usage: python parse_metadata.py
    import ijson

    # nasa_metadata2.json is the file downloaded from https://data.nasa.gov/data.json
    filename ='nasa_metadata2.json'
    infile = open(filename, 'rb')

    data_objects = ijson.items(infile, 'dataset')
    write_property(data_objects, prop_name)
   
parse_metadata('title')
parse_metadata('description')
parse_metadata('keyword')
parse_metadata('landingPage')
parse_metadata('language')
parse_metadata('theme')
parse_metadata('temporal')
parse_metadata('spatial')
parse_metadata('modified')