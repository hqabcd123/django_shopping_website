
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
    
    def get_user_data(self):
        return self.user
    
    
    
def sepraite_dict(user):
    """set all type of dict to a unit column

    Returns:
        list: Now self.user is calling by reference so want we change it
        it change 
    """
    
    param_product_name = {
        'username': [],
    }
    param_product_type = {
        'username': [],
    }
    print('####'*40)
    print(user)
    list_to_dict(user)
    print(user)
    print('####'*40)
    for u in user:
        for username, data in u.items():
            param_product_name['username'].append(username)
            param_product_type['username'].append(username)
            for i in data['product_name']:
                for k, v in i.items():
                    if k not in param_product_name:
                        print(' product: {} '.format(k))
                        param_product_name[k] = []
            for i in data['product_type']:
                for k, v in i.items():
                    if k not in param_product_type:
                        param_product_type[k] = []
                        
        for username, data in u.items():
            for product in param_product_name:
                print(product)
            
            
    print(param_product_name)
    
    return param_product_name


def list_to_dict(user1):
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
    
    
db.to_db()

"""
0   username    {product name}
1   name        1
2
3
4
5

"""


con = sqlite3.connect('./userdata.db')
cursor = con.cursor()
cursor.execute(" SELECT * FROM userdata ")
name = list(map(lambda x: x[0], cursor.description))
print('*****'*20)
print(name)

user = user_data()

for row in cursor.execute(" SELECT * FROM userdata "):
    user.set_data(row)
user.count_product_type()
dic = user.user
dic = sepraite_dict(dic)
print(user.user)
df = pd.DataFrame(dic)
print('===================================================')
print(df)