import pandas as pd
import userdata_to_db as db
import sqlite3

class user_data():
    
    def __init__(self) -> None:
        self.data = []
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
    def set_data(self, data):
        username = data[2]
        product_name = data[3]
        product_type = data[4]
        is_data_save = False
        
        for cell in self.data:
            if username ==  cell['username']:
                cell['data']['product_name'].append(product_name)
                cell['data']['product_type'].append(product_type)
                is_data_save = True
                break
        
        if not is_data_save:
            self.data.append({
                'username': username,
                'data': {
                    'product_name': [product_name],
                    'product_type': [product_type],
                }
            })
        pass
    
    def count_product_type(self):
        for user in self.data:
            for k, v in user.items():
                print(' key: {}, value {} '.format(k, v))
                #v['product_name']
                pass
        pass

db.to_db()

con = sqlite3.connect('./userdata.db')
cursor = con.cursor()
cursor.execute(" SELECT * FROM userdata ")
name = list(map(lambda x: x[0], cursor.description))
print('*********************************************************')
print(name)

user = user_data()

for row in cursor.execute(" SELECT * FROM userdata "):
    user.set_data(row)
user.count_product_type()

