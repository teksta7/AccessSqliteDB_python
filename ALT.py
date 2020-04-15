#WIP
import pandas as pd
import sqlite3
import os
from datetime import datetime

path = os.getcwd()
print(path)
print("Beginning connection...")
con = sqlite3.connect("ChatStorage.sqlite")
print("Connection successful, querying...")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con)
print("Query ok, showing high level tables...")
print(tables)
print("Querying for available messages...")
df = pd.read_sql_query("SELECT * from ZWAMESSAGE", con)
print("Query ok, showing message info...")
print('\n'.join([str(i+1)+' '+x for i, x in enumerate(df.columns)]))
#print(datetime.fromtimestamp(df.ZMESSAGEDATE.iloc[0]))
timestamp_to_apple = lambda x: datetime.fromtimestamp(x) + (datetime(2001,1,1) - datetime.fromtimestamp(0))
#print(df.ZMESSAGEDATE.iloc[0])
#print(timestamp_to_apple(df.ZMESSAGEDATE.iloc[0]))
#Methods for searching for messages
get_df_by_number = lambda df, num: df[df.ZTOJID.str.contains(num).fillna(False) | df.ZFROMJID.str.contains(num).fillna(False)]
get_df_by_contact_name = lambda df, name: df[df.ZPUSHNAME.str.contains(name).fillna(False)]
get_df_by_chat_session_id = lambda df, sid: df[df.ZCHATSESSION == sid]
grep_for_message_text = lambda df, txt: df[df.ZTEXT.str.contains(txt).fillna(False)]

print("Making dates human readable from WhatsApp") 
df['Date'] = df.ZMESSAGEDATE.apply(timestamp_to_apple)
df.index = df.Date    
df = df.sort_index() 
df.head()

df2 = get_df_by_number(df, '7')
print(len(df2))
print(list(df2.ZTEXT))

df3 = pd.read_sql_query("SELECT ZPUSHNAME from ZWAMESSAGE", con)

#print(df3)
#print('\n'.join([str(i+1)+' '+x for i, x in enumerate(df3.)]))
print(len(df3))


print("Closing connection...")
con.close()

