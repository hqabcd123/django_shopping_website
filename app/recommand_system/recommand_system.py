from numpy import product
import pandas as pd
import userdata_to_db as db
import sqlite3



class user_data():
    
    def __init__(self) -> None:
        self.data = []
        self.user = []
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
    
    def get_count(self, index):
        count = []
        for data in index:
            if data not in count or len(count) == 0:
                count.append(data)
                count.append(1)
            else:
                count[count.index(data)+1] += 1
            pass
        return count
    
    def count_product_type(self):
        print(self.data)
        for user in self.data:
            index = user['data']['product_name']
            product_name = self.get_count(index)
            index = user['data']['product_type']
            product_type = self.get_count(index)
            dict = {
                user['username']: {
                    'product_name': product_name,
                    'product_type': product_type,
                }
            }
            print(dict)
            self.user.append(dict)
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

df = pd.DataFrame(user.user)
print('===================================================')
print(df)