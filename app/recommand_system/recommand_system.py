import pandas as pd
import userdata_to_db as db
import sqlite3

class user_data():
    
    def __init__(self, data) -> None:
        self.data = []
        for row in data:
            self.data.append(list(row))
        pass

db.to_db()

con = sqlite3.connect('./userdata.db')
cursor = con.cursor()
cursor.execute(" SELECT * FROM userdata ")
name = list(map(lambda x: x[0], cursor.description))
print('*********************************************************')
print(name)
temp = []
for row in cursor.execute(" SELECT * FROM userdata "):
    temp.append(row)
    print(row)
