'''
Created on 2019年5月21日

@author: bkd
'''
from os.path import expanduser,join
import sqlite3

db_file = join(expanduser("~"),".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db")

def add_line(line_name):
    run_sql("insert into line (name) values('{}')".format(line_name))
def delete_line(line_name):
    run_sql("delete from line where name = '{}'".format(line_name))
def get_all():
    return run_sql("select id,name from line")
def modify_line(lineId,new_name):
    return run_sql("update line set name='{}' where id='{}'".format(new_name,lineId))

def run_sql(sql):    
    conn = sqlite3.connect(db_file)
    cs = conn.cursor()
    print("execute sql:" + sql )
    cs.execute(sql)
    if "select" in sql:
        return cs.fetchall()  
    conn.commit()