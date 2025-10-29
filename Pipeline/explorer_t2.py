#!/usr/bin/env python
# coding: utf-8

import hashlib
import re
from datetime import datetime, timezone
import pandas as pd
import sqlite3


EXCLUSION_LIST = ['BLANK', '-', 'NA', 'NONE', '{NULL}', 'VIDE']


# clean column names
def clean_cols(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df


def clean_dob(dob, age):
    if dob > datetime.now() and age < 100:
        dob = dob.replace(year=datetime.now().year - age)
    if age >= 100 and dob.year > datetime.now().year - 100:
        dob = dob.replace(year=datetime.now().year - age)
    return dob


def clean_column(value, exclusions=EXCLUSION_LIST):
    if isinstance(value, str) and value.strip().upper() in exclusions:
        return None
    elif isinstance(value, float) and pd.isna(value):
        return None
    else:
        return value


def hash_password(pw: str) -> str:
    if pw is None:
        return None
    else:
        return hashlib.sha256(pw.encode('utf-8')).hexdigest()


def clean_salary(salary: str, period:int=1) -> float:
    if salary is None:
        return None
    else:
        salary = (int(re.sub(r'[^\d]', '', salary))/100) * period
        return salary


def clean_phone_number(df:pd.DataFrame, column:str) -> pd.DataFrame:
    df[column] = df[column].str.replace(' ', '')
    return df


fr_mapping_columns = {
    'Prénom': 'first_name',
    'Nom de famille': 'surname',
    'DdN': 'dob',
    '\nÂge dernier anniversaire': 'age_last_birthday',
    'Couleur préférée': 'favourite_colour',
    'Animal préféré': 'favourite_animal',
    'Plat préféré': 'favourite_food',
    'Genre': 'gender',
    'Mot de passe': 'password',
    'Ville': 'city',
    'Département': 'county',
    'Code postal': 'postcode',
    'Adresse électronique': 'email',
    'Téléphone': 'phone',
    'Portable ': 'mobile',
    'BAC+': 'education',
    ' Salaire ': 'salary',
    'Visites du site Web au cours des 30 derniers jours': 'website_visits_last_30_days'
 }


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


def transform_users_df(users:pd.DataFrame,
                       country_code:str,
                       currency:str='GBP',
                       salary_period:int=1,
                       mapping_gender=None,
                       mapping_education=None):
    for col in users.columns:
        users[col] = users[col].apply(lambda x: clean_column(x, EXCLUSION_LIST))
    # hash passwords
    users['password'] = users['password'].apply(hash_password)
    # clean dob
    users['dob'] = users.apply(lambda x: clean_dob(x['dob'], x['age_last_birthday']), axis=1)
    # clean gender
    if mapping_gender:
        users['gender'] = users['gender'].replace(mapping_gender)
    # clean phone numbers
    clean_phone_number(users, 'phone')
    clean_phone_number(users, 'mobile')
    # clean salary
    users['salary'] = users['salary'].apply(lambda x: clean_salary(x, salary_period))
    users['currency'] = currency
    # add rqf column if it doesn't exist
    if mapping_education and 'rqf' not in users.columns:
        users['rqf'] = users['education'].map(mapping_education)
    # add country code
    users['country_code'] = country_code
    return users


fr_mapping_gender = {'F':'Female', 'M': 'Male', 'NB': 'Non-Binary'}


fr_mapping_education = {
    'Baccalauréat':3,
    'Licentiate':6,
    'Master':7,
    'CFA':5,
    'Collège':1,
    'Lycée':2,
    'Doctorat':8
    }


users_uk = load_user_data('data/UK User Data.csv',
                          encoding='latin1')
users_uk = transform_users_df(users_uk,
                              country_code='UK')
users_fr = load_user_data('data/FR User Data.csv',
                          date_format='%y-%m-%d',
                          mapping=fr_mapping_columns)
users_fr = transform_users_df(users_fr,
                              country_code='FR',
                              currency='EUR',
                              salary_period=12,
                              mapping_gender=fr_mapping_gender,
                              mapping_education=fr_mapping_education)


def load_login_data(filepath:str,timezone:str='Europe/London'):
    df = pd.read_csv(filepath)
    df.columns = ['login_id', 'username', 'login_timestamp']
    df.drop(columns=['login_id'], inplace=True)
    df['login_timestamp'] = pd.to_datetime(df['login_timestamp'], unit='s', utc=False)
    df['login_timestamp'] = df['login_timestamp'].dt.tz_localize(timezone).dt.tz_convert('UTC')
    return df


logins_uk = load_login_data('data/UK-User-LoginTS.csv')
logins_fr = load_login_data('data/FR-User-LoginTS.csv', timezone='Europe/Paris')


with open('create_database.sql', 'r', encoding='utf-8') as f:
    create_sql = f.read()
conn = sqlite3.connect('customers.db')
try:
    conn.executescript(create_sql)
    users_uk.to_sql('users', conn, if_exists='append', index=False)
    users_fr.to_sql('users', conn, if_exists='append', index=False)
    logins_uk.to_sql('logins', conn, if_exists='append', index=False)
    logins_fr.to_sql('logins', conn, if_exists='append', index=False)
    conn.commit()
finally:
    conn.close()

