import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import warnings


def main():
    adult_train_data, adult_test_data = import_adult_data()
    adult_train_data, adult_test_data = clean_data(adult_train_data, adult_test_data)
    adult_train_data, adult_test_data = one_hot_encoding(adult_train_data, adult_test_data)
    output_as_csv(adult_train_data, adult_test_data)

def import_adult_data():

    adult_train_data = pd.read_csv("../data/adult/raw/adult.data", header=None)
    # We need to ignore the first line of the test dataset:
    adult_test_data = pd.read_csv("../data/adult/raw/adult.test", header=None, skiprows=[0])
    # assign column names to imported data
    data_set_columns = {0:'age', 1:"workclass", 2:'fnlwgt',
                    3:'education', 4:'education-num', 
                    5:'marital-status', 6:'occupation',
                    7:'relationship', 8:'race',
                    9:'sex', 10:'capital-gain', 
                   11:'capital-loss', 12:'hours-per-week',
                   13:'native-country', 14:'annual-income'}
    # loop through columns and rename them
    for i in range(len(data_set_columns)):
        adult_train_data = adult_train_data.rename(columns = {i: data_set_columns[i]})
        adult_test_data = adult_test_data.rename(columns = {i: data_set_columns[i]})

    return adult_train_data, adult_test_data

def clean_data(adult_train_data,adult_test_data):
    adult_test_data['annual-income'] = adult_test_data['annual-income'].str.replace(".", "")
    for i in adult_train_data.columns:
        try:
            adult_train_data[i] = adult_train_data[i].str.replace(" ", "")
            adult_train_data = adult_train_data.loc[adult_train_data[i] != '?']
            x = list(adult_train_data[i].unique())
            adult_test_data[i] = adult_test_data[i].str.replace(" ", "")
            adult_test_data = adult_test_data.loc[adult_test_data[i] != '?']
            y = list(adult_test_data[i].unique())

        except:
            continue
    
    return adult_train_data, adult_test_data

# helper function for one-hot-encoding
def encode_and_bind(df, feature):
    conversion = pd.get_dummies(df[feature])
    output = pd.concat([df, conversion], axis=1)
    return output

def one_hot_encoding(adult_train_data,adult_test_data): 
    continous_data = ['workclass', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    for i in continous_data:
        adult_train_data = encode_and_bind(adult_train_data, i)
        adult_test_data = encode_and_bind(adult_test_data, i)

    adult_train_data= adult_train_data.drop(columns = continous_data)
    adult_test_data= adult_test_data.drop(columns = continous_data)
   
    return adult_train_data, adult_test_data

def output_as_csv(adult_train_data, adult_test_data):
    adult_train_data.to_csv("../data/adult/preproccessed/adult_training_set.csv", index=False)
    adult_test_data.to_csv("../data/adult/preproccessed/adult_testing_set.csv", index=False)


if __name__ == '__main__':
    main()
