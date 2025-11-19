import logging
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 

# duplicates
def check_duplicates(df:pd.DataFrame) -> None:
    num_dupes = df.duplicated().sum()
    if num_dupes > 0:
        logging.info(f"Found {num_dupes} duplicate rows")
    else:
        logging.info("No duplicate rows found")

# email uniqueness
def check_email_uniqueness(df:pd.DataFrame, subset=['email']) -> None:
    num_dupes = df.duplicated(subset=subset).sum()
    if num_dupes > 0:
        logging.info(f"Found {num_dupes} duplicate emails")
    else:
        logging.info("No duplicate emails found") 