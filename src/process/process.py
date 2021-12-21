import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
import json
import math
import logging
import csv

def get_env_var(file):
    load_dotenv(file)
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    DB_HOST = os.getenv('DB_HOST')
    return POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, DB_HOST

def connect_database(credentials):
    POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, DB_HOST = get_env_var(credentials)
    conn = psycopg2.connect(dbname=POSTGRES_DB, host=DB_HOST ,user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur, conn

def create_table(cur, conn, query):
    cur.execute(query)
    conn.commit()

def row_factory(row):
    return [x if x != '' else 'NaN' for x in row]

def readCSV(filename):
    ratings_list = []
    with open('./data/' + filename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            '''if(row[len(row)-1] == ','):
                row = row[:-1]'''
            print(row_factory(row))
            ratings_list.append(row_factory(row))
        ratings_list.pop(0)
    return ratings_list

def insert_in_table(cur, table_list, table_insert_query):
    for row in table_list:
        cur.execute(table_insert_query, row)








#ratings = readCSV('ratings.csv')
#for index, row in ratings.iterrows():
#    print(row_factory(row_factory(row['rating_id']), row_factory(row['description']), row_factory(row['rating'])))