# Create finance lib for this project by using yahoo finance api
import yfinance as yf
import pandas as pd

# set dataframe for modifying historical data
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:.2f}'.format)

# ticker_name = 'TSLA' # Tesla
# ticker_name = 'BAC' # Bank of America
# ticker_name = 'AXP' # American Express
# ticker_name = '035420.KS' # NAVER
# ticker_name = '024110.KS' # 기업은행
# ticker_name = 'LMT'  # Lockheed Martin
# ticker_name = 'BA'  # Boeing
# ticker_name = 'NOC'  # Northrop Grumman
# ticker_name = 'HON'  # Honeywell
# ticker_name = 'SPCE'  # Virgin Galactic
# ticker_name = 'RTX'  # Raytheon Technologies
# ticker_name = 'PM'  # Philip Morris International
# ticker_name = '028670.KS'  # PAN OCEAN
ticker_name = 'CB'  # Chubb
default_period = 'max'

finance_tick = yf.Ticker(ticker_name)
