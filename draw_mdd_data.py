# View the avg of the Max Draw down of the database each year by using product name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from lib import TABLE_NAME, COLUMN_NAME_ARRAY
from lib.database import SQlite3Database as database

images_dir = './images'

# Read the data from the database
db = database()
db_data = db.read(TABLE_NAME)
db_schema = db.sqlite_table_schema(TABLE_NAME)

# Convert the data to dataframe
default_df = pd.DataFrame(
    db_data,
    columns=db_schema,
)

# Get the product name(unique)
# product name is Key
product_name = default_df['key'].unique()

print(product_name)

for product in product_name:
    # Draw the data By using product name
    plt.figure(figsize=(20, 10))
    plt.ylabel('Max Draw Down')
    plt.xlabel('Year')
    plt.title('Max Draw Down of the Product')
    plt.grid(True)

    # Get the data by using product name
    product_df = default_df[default_df['key'] == product]

    # Get the year(unique)
    year = product_df['Year'].unique()

    # Get the Max Draw Down of the product each year
    mdd = product_df['Max_Drawn_Down']

    # Draw the data
    plt.plot(
        year,
        mdd,
        label=product,
    )

    # Save the image
    # if there is no images_dir, create it
    file_name = f'{images_dir}/{product}.png'
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)

    # if there is the image, remove it
    if os.path.exists(file_name):
        os.remove(file_name)

    plt.savefig(f'{images_dir}/{product}.png')
