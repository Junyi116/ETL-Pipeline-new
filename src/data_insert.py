
import pandas as pd
import sqlite3
def insert_transformed_data(df):
    """Function that inserts transformed data into the database"""
    conn = sqlite3.connect("../../data/bootcamp_db")
    df.to_sql('online_transactions_cleaned', conn, if_exists='replace', index=False)
    print("The data has been inserted into the database table 'online_transactions_cleaned'")
    conn.close()