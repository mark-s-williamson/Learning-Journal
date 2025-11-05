import hashlib
import re
from datetime import datetime
import pandas as pd

def clean_cols(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def clean_dob(dob, age):
    if dob > datetime.now() and age < 100:
        dob = dob.replace(year=datetime.now().year - age)
    if age >= 100 and dob.year > datetime.now().year - 100:
        dob = dob.replace(year=datetime.now().year - age)
    return dob

def clean_column(value, exclusions:list):
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

def clean_salary(salary:str, period:int=1) -> float:
    if salary is None:
        return None
    else:
        salary = (int(re.sub(r'[^\d]', '', salary))/100) * period
        return salary

def clean_phone_number(number:str) -> str:
    return re.sub(r'[^\d]', '', number)

def transform_users_df(users:pd.DataFrame,
                       exclusions:list,
                       country_code:str,
                       currency:str='GBP',
                       salary_period:int=1,
                       mapping_gender=None,
                       mapping_education=None):
    for col in users.columns:
        users[col] = users[col].apply(lambda x: clean_column(x, exclusions))
    # hash passwords
    users['password'] = users['password'].apply(hash_password)
    # clean dob
    users['dob'] = users.apply(lambda x: clean_dob(x['dob'], x['age_last_birthday']), axis=1)
    # clean gender
    if mapping_gender:
        users['gender'] = users['gender'].replace(mapping_gender)
    # clean phone numbers
    users['phone'] = users['phone'].apply(clean_phone_number)
    users['mobile'] = users['mobile'].apply(clean_phone_number)
    # clean salary
    users['salary'] = users['salary'].apply(lambda x: clean_salary(x, salary_period))
    users['currency'] = currency
    # add rqf column if it doesn't exist
    if mapping_education and 'rqf' not in users.columns:
        users['rqf'] = users['education'].map(mapping_education)
    # add country code
    users['country_code'] = country_code
    return users