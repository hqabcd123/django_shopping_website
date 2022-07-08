from logging import error
import sqlite3

class user_history_class():

    def __init__(self, *args, **kwargs) -> None:
        self.userdata = []
        self.temp = args[0]
        self.count_history()
        pass

    def count_history(self) -> None :
        for cell in self.temp:
            if cell['username'] in self.userdata:
                self.userdata = cell['username']
            else:
                self.userdata.append({
                    '1.click_date': cell['click_date'],
                    '2.username': cell['username'],
                    '3.product_name': cell['product_name'],
                    '4.product_type': list(cell['product_type']),
                })
        pass
    
    def get_userdata(self) -> list :
        return self.userdata

def link_string(*args) -> str :
    temp = ''
    for data in args:
        temp += '{} varchar(50), '.format(data)
    temp = temp[:-2]
    return temp

class order_dict_list():
    
    def __init__(self, dic) -> None:
        self.index = []
        self.list_of_dict = []
        for key in dic:
            self.index.append(key)
        self.index = self.sort_dict()
        for i in self.index:
            if type(dic[i]) == list:
                for temp in dic[i]:
                    self.list_of_dict.append(temp)
            else:
                self.list_of_dict.append(dic[i])
    
    def sort_dict(self):
        ind = self.index
        for i in range(len(ind)-1):
            for j in range(len(ind)-i-1):
                if int(ind[j][0]) > int(ind[j+1][0]):
                    temp = ind[j]
                    ind[j] = ind[j+1]
                    ind[j+1] = temp
        return ind
    
    def get_list_of_dict(self):
        return self.list_of_dict
    
    def get_index(self):
        for i in range(len(self.index)):
            self.index[i] = self.index[i][2:]
        return self.index


def to_db():

    username = []
    history = []
    product_borad = []
    Data = []
    user_history = []
    temp = []


    con = sqlite3.connect('../../db.sqlite3')
    cursor = con.cursor()


    for row in cursor.execute('SELECT username FROM app_user'):
        username.append(row)

    for name in username:
        for row in cursor.execute( "SELECT foodprint_set_id FROM app_user_history_set WHERE username = '{}' ".format(name[0])):
            history.append({
                'username': name[0],
                'foodprint_set_id': row[0],
            })

    for cell in history:
        for row in cursor.execute(" SELECT foodprint_id, click_date FROM app_user_history WHERE id = '{}' ".format(cell['foodprint_set_id'])):
            product_borad.append({
                'username': cell['username'],
                'product_id': row[0],
                'click_date': row[1],
            })

    for cell in product_borad:
        for row in cursor.execute(
            " SELECT product_name, product_code_id FROM app_product_borad WHERE id = '{}' ".format(cell['product_id'])
        ):
            Data.append({
                'username': cell['username'],
                'click_date': cell['click_date'],
                'product_name': row[0],
                'product_code_id': row[1],
            })

    for cell in Data:
        for row in cursor.execute(
            " SELECT set_of_product_type_id FROM app_set_of_product_type WHERE product_code_id = '{}' ".format(cell['product_code_id'])
        ):
            for i in cursor.execute(
                " SELECT product_type FROM app_product_type WHERE id = '{}' ".format(row[0])
            ):
                user_history.append({
                    'click_date': cell['click_date'],
                    'username': cell['username'],
                    'product_name': cell['product_name'],
                    'product_type': i,
                })

    del(username, product_borad, Data)
    user_data = user_history_class(user_history)

    con.close()

    con = sqlite3.connect('./userdata.db')
    cursor = con.cursor()
    sql =  " CREATE TABLE IF NOT EXISTS userdata "
    sql += "(id int, click_date datetime, username varchar(100), product_name varchar(400), product_type longtext ) "

    cursor.execute(sql)
    
    id = 0
    for row in cursor.execute(" SELECT * FROM userdata "):
        id += 1
    #name = list(map(lambda x: x[0], cursor.description))#get the column name from table
    
    print('id: ' + str(id))
    dict_userdata = user_data.get_userdata()[id:]
    
    for row in dict_userdata:
        order = order_dict_list(row)
        parma = order.get_list_of_dict()
        parma = tuple(parma)  #','.join(parma)
        parma = (id,) + parma
        print(parma)
        sql = "  INSERT INTO userdata VALUES (?, ?, ?, ?, ?) "
        cursor.execute(sql, parma)
        id += 1
    con.commit()

    con.close()