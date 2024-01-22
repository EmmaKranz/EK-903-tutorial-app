import pandas as pd

def read_data(filepath):
    #TODO write docstring
    """Reads in CSV from filepath and returns dataframe for analysis.
    Inputs: filepath -> string : path to csv
    Outputs: df -> Dataframe: Dataframe for analysis
    """

    df = pd.read_csv(filepath)
    return df

def ingress(df):
    #TODO convert the birthday column to datetimes
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    return df

def gender_count(df): 
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    return len(df['CHILD'].unique())
