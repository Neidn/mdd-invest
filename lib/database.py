import pandas as pd
import sqlite3
from . import *


# Class for database
# Read, Write, Update, Delete From Dataframe
class SQlite3Database:
    def __init__(self):
        self.con = sqlite3.connect(SQlite3_DATABASE)
        self.cur = self.con.cursor()

    # create table if not exists
    def create_table(self, table_name, column_name_array):
        self.cur.execute(
            f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(column_name_array)})'
        )

    # drop table if exists
    def drop_table(self, table_name):
        self.cur.execute(
            f'DROP TABLE IF EXISTS {table_name}'
        )

    # Procedure for insert data into table.id
    # id: uuid
    def insert_uuid(self, table_name):
        self.cur.execute(
            f'UPDATE {table_name} SET id = uuid()'
        )

    # Read data from table
    def read(self, table_name):
        self.cur.execute(
            f'SELECT * FROM {table_name}'
        )
        return self.cur.fetchall()

    # Read schema from table
    def sqlite_table_schema(self, table_name):
        self.cur.execute(
            f'PRAGMA table_info({table_name})'
        )
        schema_array = []

        for schema in self.cur.fetchall():
            schema_array.append(schema[1])

        return schema_array

    # Write data to table
    def write(self, table_name, dataframe):
        dataframe.to_sql(
            table_name,
            self.con,
            if_exists='append',
            index=False,
        )

    # Update data to table
    def update(self, table_name, dataframe):
        dataframe.to_sql(
            table_name,
            self.con,
            if_exists='replace',
            index=False,
        )

    # Delete data from table
    def delete(self, table_name, dataframe):
        dataframe.to_sql(
            table_name,
            self.con,
            if_exists='replace',
            index=False,
        )

    # Delete data from table by using key and year
    def delete_data(self, table_name, key, year):
        self.cur.execute(
            f'DELETE FROM {table_name} WHERE key = "{key}" AND Year = "{year}"'
        )

    # Check data from table
    def check_data(self, table_name, key, year):
        self.cur.execute(
            f'SELECT * FROM {table_name} WHERE key = "{key}" AND Year = "{year}"'
        )
        return self.cur.fetchall()

    # Close database
    def close(self):
        self.con.close()
