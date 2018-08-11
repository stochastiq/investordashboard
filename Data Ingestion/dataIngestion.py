# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:29:05 2018

@author: abiga
"""

import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
import pandas as pd
from sqlalchemy import create_engine

data = yf.download('AAPL','2016-01-01','2018-01-01')
data.Close.plot()
plt.show()

tickers = ['AAPL', 'GOOGL', 'ASX']
startDate = '2016-01-01'
endDate = '2018-01-01'

df = pd.DataFrame(columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'ticker'])

for t in tickers:
    data = yf.download(t, startDate, endDate)
    data['ticker'] = t
    df = df.append(data, ignore_index = True)
    
df.shape
df.ticker.unique()

connection_string = "ajlowdb.c7svw9hibdow.ap-southeast-1.rds.amazonaws.com:1808/investordb"

user = 'stochastiq'
pw = 'wengwengweng'
host = 'ajlow.c7svw9hibdow.ap-southeast-1.rds.amazonaws.com'
port = '1808'
dbname = 'investordb'

engine = create_engine('postgresql://'+user+':'+pw+'@'+host+':'+port+'/'+dbname,echo=False)
df.to_sql('df', con=engine, if_exists = 'replace', index=False)

retrieved = pd.read_sql('SELECT * FROM df', engine)

 
 