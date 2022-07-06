import sqlite3
from numpy import product
import pandas as pd

class user_history_class():

    def __init__(self, *args, **kwargs) -> None:
        self.userdata = []
        print(args[0])
        self.temp = args[0]
        pass

    def count_history(self):
        for cell in self.temp:
            if cell['username'] in self.userdata:
                self.userdata = cell['username']
            else:
                
                self.userdata.append({
                    'username': cell['username'],
                    #
                })
        pass

def link_string(*args) -> str :
    temp = ''
    for data in args:
        temp += '{} varchar(50), '.format(data)
    temp = temp[:-2]
    return temp

username = []
history = []
product_borad = []
Data = []
user_history = []


con = sqlite3.connect('../db.sqlite3')
cursor = con.cursor()


for row in cursor.execute('SELECT username FROM app_user'):
    username.append(row)
    print(row)

for name in username:
    for row in cursor.execute( "SELECT foodprint_set_id FROM app_user_history_set WHERE username = '{}' ".format(name[0])):
        history.append({
            'username': name[0],
            'foodprint_set_id': row[0],
        })

for cell in history:
    for row in cursor.execute(" SELECT foodprint_id FROM app_user_history WHERE id = '{}' ".format(cell['foodprint_set_id'])):
        product_borad.append({
            'username': cell['username'],
            'product_id': row[0],
        })

for cell in product_borad:
    for row in cursor.execute(
        " SELECT product_name, product_code_id FROM app_product_borad WHERE id = '{}' ".format(cell['product_id'])
    ):
        Data.append({
            'username': cell['username'],
            'product_name': row[0],
            'product_code_id': row[1],
        })
print(Data)

for cell in Data:
    for row in cursor.execute(
        " SELECT set_of_product_type_id FROM app_set_of_product_type WHERE product_code_id = '{}' ".format(cell['product_code_id'])
    ):
        for i in cursor.execute(
            " SELECT product_type FROM app_product_type WHERE id = '{}' ".format(row[0])
        ):
            print(' username: {} click product : {} \n which is {} '.format(
                cell['username'], cell['product_name'], i[0]
            ))
            user_history.append({
                'username': cell['username'],
                'product_name': cell['product_name'],
                'product_type': i,
            })

del(username, product_borad, Data)
temp = user_history_class(user_history)

con.close()

con = sqlite3.connect('./userdata.db')
cursor = con.cursor()

str1 = link_string('shoes', 'range', 'pants', 'shirt')
print(str1)

cursor.execute(
    " CREATE TABLE IF NOT EXISTS userdata(username varchar(50), prodcut_name varchar(50), {} ) ".format(str1)
)

table = cursor.execute(
    " SELECT * FROM userdata "
)
name = list(map(lambda x: x[0], cursor.description))#get the column name from table
print(table.fetchall())
print(name)