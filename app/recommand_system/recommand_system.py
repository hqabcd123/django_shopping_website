import numpy as np
from distutils.log import error
import pandas as pd
import userdata_to_db as db
import sqlite3
from sklearn.metrics.pairwise import paired_distances,cosine_similarity



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
            self.user.append(dict)
        pass
    
    def list_to_dict(self, user1):
        user = user1
        for i in user:
            for username, data in i.items():
                for product in data:
                    temp = []
                    temp_key = ''
                    for j in range(len(data[product])):
                        if j%2 == 0:
                            temp_key = data[product][j]
                        else:
                            temp.append({
                                temp_key :data[product][j]
                            })
                            temp_key = ''
                    #print(temp)
                    data[product] = temp
    
    
    def sepraite_dict(self):
        """set all type of dict to a unit column

        Returns:
            list: Now self.user is calling by reference so want we change it
            it change 
        """
        user = self.user
        param_product_name = {
            'username': [],
        }
        param_product_type = {
            'username': [],
        }
        self.list_to_dict(user)
        for u in user:
            for username, data in u.items():
                param_product_name['username'].append(username)
                param_product_type['username'].append(username)
                for i in data['product_name']:
                    for k, v in i.items():
                        if k not in param_product_name:
                            param_product_name[k] = []
                for i in data['product_type']:
                    for k, v in i.items():
                        if k not in param_product_type:
                            param_product_type[k] = []
        
        for u in user:                    
            for username, data in u.items():
                temp = []
                for i in data['product_name']:
                    for k, v in i.items():
                        ###################################################################################
                        param_product_name[k].append(v)
                        temp.append(k)
                for k in param_product_name:
                    if k not in temp and k != 'username':
                        param_product_name[k].append(0)
                        temp.append(k)
        for u in user:                    
            for username, data in u.items():
                temp = []
                for i in data['product_type']:
                    for k, v in i.items():
                        ###################################################################################
                        param_product_type[k].append(v)
                        temp.append(k)
                for k in param_product_type:
                    if k not in temp and k != 'username':
                        param_product_type[k].append(0)
                        temp.append(k)                    
            
        print(param_product_name)
        
        return [param_product_name, param_product_type]

def create_matrix(list):
    product = {
        'product_name':[],
    }
    print('#################create matrix#################')
    print('===='*40)
    for row in list:
        product[row[1]] = []
        product['product_name'].append(row[0])
        pass
    for key in product:
        for row in list:
            temp_str = ''
            if row[1] != key and key != 'product_name':
                product[key].append(0)
            elif row[1] == key and key != 'product_name':
                product[key].append(1)
                
    return product
        


db.to_db()

"""
0   username    {product name}
1   name        1
2
3
4
5

"""

product_type = []
con = sqlite3.connect('./userdata.db')
cursor = con.cursor()
cursor.execute(" SELECT * FROM userdata ")
name = list(map(lambda x: x[0], cursor.description))
print('*****'*20)
print(name)

user = user_data()

for row in cursor.execute(" SELECT * FROM userdata "):
    user.set_data(row)
    
for row in cursor.execute(" SELECT product_name, product_type FROM product_type "):
    print('row: {} '.format(row))
    product_type.append([row[0], row[1]])

con.close()
user.count_product_type()
user = user.sepraite_dict()

df = pd.DataFrame(user[1])
user_vec = df.groupby('username').mean()
product_type = create_matrix(product_type)
print(product_type)
product_vec = pd.DataFrame(product_type)
product_vec = product_vec.groupby('product_name').mean()


print('===='*40)
print(df)
print(user_vec)
print(product_vec)
print('===='*40)