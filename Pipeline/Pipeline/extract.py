import pandas as pd
from .transform import clean_cols

def load_user_data(filepath:str,
                   encoding:str='utf-8',
                   date_format:str='%d/%m/%y',
                   mapping=None):
    df = pd.read_csv(filepath, encoding=encoding)
    if mapping:
        df.rename(columns=mapping, inplace=True)
    df = clean_cols(df)
    df['dob'] = pd.to_datetime(df['dob'], format=date_format, errors='coerce')
    return df

def load_login_data(filepath:str,timezone:str='Europe/London'):
    df = pd.read_csv(filepath)
    df.columns = ['login_id', 'username', 'login_timestamp']
    df.drop(columns=['login_id'], inplace=True)
    df['login_timestamp'] = pd.to_datetime(df['login_timestamp'], unit='s', utc=False)
    df['login_timestamp'] = df['login_timestamp'].dt.tz_localize(timezone).dt.tz_convert('UTC')
    return df