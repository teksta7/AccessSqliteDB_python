import pandas as pd
import sqlite3
import os
from datetime import datetime

path = os.getcwd()
print(path)
print("Beginning connection...")
conn = None
try:
	conn = sqlite3.connect("ChatStorage.sqlite")
except Error as e:
	print(e)

cur = conn.cursor()
cur.execute("SELECT * FROM ZWAMESSAGE")

rows = cur.fetchall()

for row in rows:
    print(row)