from numpy import unique, isnan
from pandas import DataFrame
from . import finance_tick, default_period, ticker_name


# Process historical data
# Convert historical data to new dataframe
class Hist:
    def __init__(self):
        # get historical market data
        hist = finance_tick.history(
            period=default_period,
            interval='1d',
            auto_adjust=True,
        )

        self.modified_hist = hist.loc[:, ['Close']]

        self.column_array = None
        self.index_array = None
        self.create_array()

    def create_array(self):
        # index array for new dataframe
        # date format = '%Y'
        # Remove duplicate index
        self.index_array = unique(
            self.modified_hist.index.strftime('%Y')
        )

        # column array for new dataframe
        # date format = '%m-%d'
        # Remove duplicate column
        self.column_array = unique(
            self.modified_hist.index.strftime('%m-%d')
        )

    def create_dataframe(self):
        # make new dataframe
        new_dataframe = DataFrame(
            columns=self.column_array,
            index=self.index_array,
        )

        # fill new dataframe
        for i in range(len(self.modified_hist)):
            new_dataframe.loc[
                self.modified_hist.index[i].strftime('%Y'), self.modified_hist.index[i].strftime('%m-%d')] = \
                self.modified_hist.iloc[i, 0]

        return new_dataframe


# Modify new dataframe
# Add new columns to new dataframe
class Modify:
    def __init__(self, index_array):
        self.dataframe = DataFrame(
            columns=['Max_Rise_Percent', 'Max_Drawn_Down', 'Max', 'Min', 'First_Date', 'First', 'Year'],
            index=index_array,
        )
        self.add_column()

    def add_column(self):
        # add some columns to result dataframe
        self.dataframe['key'] = ticker_name

    def add_data(self, dataframe):
        self.dataframe['Year'] = dataframe.index

        self.dataframe['Max'] = dataframe.max(axis=1)
        self.dataframe['Min'] = dataframe.min(axis=1)

        self.dataframe['Max'] = self.dataframe['Max'].astype(float)
        self.dataframe['Min'] = self.dataframe['Min'].astype(float)
        self.dataframe['First'] = self.dataframe['First'].astype(float)

        # First Row is not the data of price NAN
        # So, we need to find the first date of the year
        # which is not the data of price NAN
        # and the first price of the year
        # and then add them to the new dataframe
        for i in range(len(dataframe)):
            for j in range(len(dataframe.columns)):
                if not isnan(dataframe.iloc[i, j]):
                    self.dataframe.iloc[i, 4] = dataframe.columns[j]
                    self.dataframe.iloc[i, 5] = dataframe.iloc[i, j]
                    break

        self.dataframe['Max_Rise_Percent'] = (self.dataframe['Max'] / self.dataframe['First'] - 1) * 100
        self.dataframe['Max_Drawn_Down'] = (self.dataframe['Min'] / self.dataframe['First'] - 1) * 100

        # round the result
        self.dataframe['Max_Rise_Percent'] = self.dataframe['Max_Rise_Percent'].round(2)
        self.dataframe['Max_Drawn_Down'] = self.dataframe['Max_Drawn_Down'].round(2)
