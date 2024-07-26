from finance.history import Hist, Modify
from lib.database import SQlite3Database
from lib import TABLE_NAME, COLUMN_NAME_ARRAY

history = Hist()
history_dataframe = history.create_dataframe()
history_index = history.index_array

modify = Modify(history_index)
modify.add_data(history_dataframe)

# save result dataframe to sqlite3 database
database = SQlite3Database()

# database.drop_table(TABLE_NAME)
database.create_table(TABLE_NAME, COLUMN_NAME_ARRAY)

# Check the data
# If have the same data which has the same key and year, remove it
# If not, add it
for index, row in modify.dataframe.iterrows():
    if database.check_data(TABLE_NAME, row['key'], row['Year']):
        database.delete_data(TABLE_NAME, row['key'], row['Year'])

database.write(TABLE_NAME, modify.dataframe)
