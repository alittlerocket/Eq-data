from math import floor
import json
import pandas as pd

def parse_json(filename):
    mag_list = [0 for i in range(0,10)]

    # Open the JSON file
    file = open(filename, 'r')

    # Read the file contents
    json_data = file.read()

    # Parse the JSON data
    data = json.loads(json_data)

    for eq in data['features']:
        mag = eq['properties']['mag']
        mag_list[floor(mag)] += 1
    
    return mag_list

def write_table(mag_list):
    avgs = [mag / 123 for mag in mag_list]
    will_occur = [1 / avg for avg in avgs]
    will_not =  [1-p for p in will_occur]

    data = {
        'Name' : [f'{i}-{i}.9' for i in range(0, len(mag_list))],
        'Average EQs per year' : avgs,
        'Probability of an EQ per Year' : will_occur,
        'Probability of No EQ per Year' : will_not
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)
    

if __name__ == "__main__":
    mag_list = parse_json("query.json")



        