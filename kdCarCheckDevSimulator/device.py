'''
Created on 2019年5月21日

@author: bkd
'''
from os.path import expanduser,join
import sqlite3

db_file = join(expanduser("~"),".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db")
def add_device(big_item,model,com_port,line_id):
    conn = sqlite3.connect(db_file)
    cs = conn.cursor()
    cs.execute("insert into device (big_item,model,com_port,line_id) values(?,?,?,?)",(big_item,model,com_port,line_id))
    conn.commit()
    
def delete_device(deviceId):
    run_sql("delete from device where id = '{}'".format(deviceId))
def get_all(line_id):
    return run_sql("select id,big_item,model,com_port,line_id from device where line_id ='{}'".format(line_id))
def modify_device(big_item,model,com_port,device_id):
    return run_sql("update device set big_item='{}', model ='{}', com_port='{}' where id='{}'".format(big_item,model,com_port,device_id))

def run_sql(sql):    
    conn = sqlite3.connect(db_file)
    cs = conn.cursor()
    print("execute sql:" + sql )
    cs.execute(sql)
    if "select" in sql:
        return cs.fetchall()  
    conn.commit()