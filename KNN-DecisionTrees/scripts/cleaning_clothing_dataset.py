import pandas as pd
import json
import subprocess
from cleaning_income_dataset import encode_and_bind

def main():
    # call bash script to convert json objects to a list of json objects
    rc = subprocess.call("./fix_json_for_clothing_dataset.sh")
    clothing_df = import_dataframe_and_clean()
    clothing_df = one_hot_encoding(clothing_df)
    clothing_df.to_csv("../data/clothing_fit/preproccessed/clothing_data_set.csv", index=False)
    

def import_dataframe_and_clean():
    modcloth_df = pd.read_json('../data/clothing_fit/raw/clothing_fixed_json_data.json')
    # drop unncessary columns 
    modcloth_df = modcloth_df.drop(columns=['quality','bust','shoe size', 'shoe width', 'waist', 'item_id', 'review_summary', 'review_text','user_id', 'user_name' ])
    # drop those records with missing values for the following columns
    modcloth_df = modcloth_df.dropna(subset=['bra size', 'cup size', 'height', 'hips','length'])
    return modcloth_df

def one_hot_encoding(df):
    # specify data columns to be encoded
    continous_data = ['category', 'cup size', 'fit', 'height', 'length']
    for i in continous_data:
        df = encode_and_bind(df, i)

    df= df.drop(columns = continous_data)
    return df


if __name__ == '__main__':
    main()
