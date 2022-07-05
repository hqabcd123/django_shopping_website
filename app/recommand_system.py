import sqlite3
from numpy import product
import pandas as pd


username = []
history = []
product_borad = []
Data = []


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
            'prodcut_name': row[0],
            'product_code_id': row[1],
        })
print(Data)

for cell in Data:
    for row in cursor.execute(
        " SELECT set_of_product_type FROM app_set_of_product_type WHERE product_code_id = '{}' ".format(cell['product_code_id'])
    ):
        print(row)


con.close()