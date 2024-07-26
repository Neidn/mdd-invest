# -*- coding: utf-8 -*-
# SQlite3 database to save the pandas dataframe
SQlite3_DATABASE = 'database.db'

# Historical data table name
TABLE_NAME = 'historical_data'

# Column name array for the historical data table
# id: uuid # primary key
# key: column name, ticker name
# Max_Rise_Percent : Max price of the year / First price of the year -1
# Max_Drawn_Down : Min price of the year / First price of the year -1
# Max: Max price of the year
# Min: Min price of the year
# First_Date: First date of the year which is the first price of the year(which is not the data of price NAN)
# First: First price of the year
COLUMN_NAME_ARRAY = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT',
    'key TEXT',
    'Year TEXT',
    'Max_Rise_Percent REAL',
    'Max_Drawn_Down REAL',
    'Max REAL',
    'Min REAL',
    'First_Date TEXT',
    'First REAL',
]

from . import *
