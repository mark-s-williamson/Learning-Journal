#!/usr/bin/env python
# coding: utf-8

import sqlite3
import json
from pipeline.extract import load_user_data, load_login_data
from pipeline.transform import transform_users_df

EXCLUSION_LIST = ['BLANK', '-', 'NA', 'NONE', '{NULL}', 'VIDE']

def load_json_config(path:str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    return

usa_mapping_columns = {
    'Last Name':'surname',
    'Favorite Color':'favourite_colour',
    'Favorite Animal':'favourite_animal',
    'Favorite Food':'favourite_food',
    'Town/City':'city',
    'Zip Code':'postcode',
    'Landline':'phone',
    'Cell Phone':'mobile'
}

usa_mapping_gender = {0:'Female', 1: 'Male'}

usa_mapping_education = {
    'High School Diploma':3,
    'Associate Degree':4,
    'Foundation Degree':5,
    'Bachelor Degree':6,
    "Master’s":7,
    'Doctorate':8
}

# load configs
config_fr = load_json_config('config/config_fr.json')

users_uk = load_user_data('data/UK User Data.csv',
                          encoding='latin1')
users_uk = transform_users_df(users_uk,
                              exclusions=EXCLUSION_LIST,
                              country_code='UK')
users_fr = load_user_data(config_fr['user_path'],
                          date_format=config_fr['date_format'],
                          mapping=config_fr['mapping_columns'])
users_fr = transform_users_df(users_fr,
                              exclusions=EXCLUSION_LIST,
                              country_code=config_fr['label'],
                              currency=config_fr['currency'],
                              salary_period=config_fr['salary_period'],
                              mapping_gender=config_fr['mapping_gender'],
                              mapping_education=config_fr['mapping_education'])
users_usa = load_user_data('data/USA User Data.csv',
                           date_format='%m/%d/%y',
                           mapping=usa_mapping_columns)
users_usa = transform_users_df(users_usa,
                               exclusions=EXCLUSION_LIST,
                               country_code='US',
                               currency='USD',
                               mapping_gender=usa_mapping_gender,
                               mapping_education=usa_mapping_education)


logins_uk = load_login_data('data/UK-User-LoginTS.csv')
logins_fr = load_login_data(config_fr['login_path'],
                            timezone=config_fr['timezone'])
logins_usa = load_login_data('data/USA-User-LoginTS.csv', timezone='US/Eastern')


with open('scripts/create_database.sql', 'r', encoding='utf-8') as f:
    create_sql = f.read()
conn = sqlite3.connect('customers.db')
try:
    conn.executescript(create_sql)
    users_uk.to_sql('users', conn, if_exists='append', index=False)
    users_fr.to_sql('users', conn, if_exists='append', index=False)
    users_usa.to_sql('users', conn, if_exists='append', index=False)
    logins_uk.to_sql('logins', conn, if_exists='append', index=False)
    logins_fr.to_sql('logins', conn, if_exists='append', index=False)
    logins_usa.to_sql('logins', conn, if_exists='append', index=False)
    conn.commit()
finally:
    conn.close()

