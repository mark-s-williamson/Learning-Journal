#!/usr/bin/env python
# coding: utf-8

import sqlite3
import json
import logging
from pipeline.extract import load_user_data, load_login_data
from pipeline.transform import transform_users_df
from tests.validation import check_duplicates, check_email_uniqueness

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

EXCLUSION_LIST = ['BLANK', '-', 'NA', 'NONE', '{NULL}', 'VIDE']

def load_json_config(path:str):
    """Load JSON config file"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# load configs
config_uk = load_json_config('config/config_uk.json')
config_fr = load_json_config('config/config_fr.json')
config_usa = load_json_config('config/config_usa.json')

def process_data(config):
    """Process user and login data based on config file"""
    logger.info(f"Loading {config['label']} user data")
    users = load_user_data(config['user_path'],
                           date_format=config['date_format'],
                           mapping=config.get('mapping_columns', None),
                           encoding=config['encoding'])
    logger.info(f"Total rows '{config['user_path']}' is {len(users)}")
    logger.info(f"Transforming {config['label']} user data")
    users = transform_users_df(users,
                               exclusions=EXCLUSION_LIST,
                               country_code=config['label'],
                               currency=config['currency'],
                               salary_period=config['salary_period'],
                               mapping_gender=config.get('mapping_gender', None),
                               mapping_education=config.get('mapping_education', None))
    check_duplicates(users)
    check_email_uniqueness(users)
    logger.info(f"Loading {config['label']} login data")
    logins = load_login_data(config['login_path'],
                             timezone=config['timezone'])

    return users, logins

users_uk, logins_uk = process_data(config_uk)
users_fr, logins_fr = process_data(config_fr)
users_usa, logins_usa = process_data(config_usa)

with open('scripts/create_database.sql', 'r', encoding='utf-8') as db_f:
    create_sql = db_f.read()
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
