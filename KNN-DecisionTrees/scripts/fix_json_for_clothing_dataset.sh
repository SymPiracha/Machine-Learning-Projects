#!/bin/bash

### The function of this script is to convert the clothing dataset file into a list of json objects instead of a json object on each line. This will make it easier to import the file as a dataframe in pandas.

# replace add comman to seperate each json object with a comman so we can create a list of json objects
sed s/$/,/ ../data/clothing_fit/raw/modcloth_final_data.json > ../data/clothing_fit/raw/clothing_fixed_json_data.json
# add '[' at the start of the file
sed -i '1s/^/[/' ../data/clothing_fit/raw/clothing_fixed_json_data.json
# remove the last two lines (new line and comma) and replace with ']'
truncate -s-2 ../data/clothing_fit/raw/clothing_fixed_json_data.json
echo "]" >> ../data/clothing_fit/raw/clothing_fixed_json_data.json
