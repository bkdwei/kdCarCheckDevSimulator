'''
Created on 2019年5月22日

@author: bkd
'''
import MySQLdb

from .cmd import cmd

from PyQt5.QtCore import QThread, pyqtSignal

class import_cmd(QThread):
    show_status_signal = pyqtSignal(str)
    def __init__(self,connect_str):
        super().__init__()
        self.connect_str = connect_str
        
        
        
    def run(self):
        dlg_cmd = cmd()
        confs = self.connect_str.split(";")
        print(confs)
        if len(confs) != 5:
            self.show_status_signal.emit("连接信息不足： "  + confs)
            return
        # 打开数据库连接
    #     db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )
        db = MySQLdb.connect(host= confs[0], port=int(confs[1]), user=confs[2], passwd=confs[3],db =confs[4], charset='utf8' )
        
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT m.model,c.cmd_value,c.cn_name from dev_cmd c join  dev_model m on c.model_id = m.id order by m.model")
        
        # 使用 fetchone() 方法获取一条数据
        cmd_list = cursor.fetchall()
        
        # 关闭数据库连接
        db.close()
        if cmd_list :
            print(cmd_list)
            for cmd_item in cmd_list :
                try:
                    dlg_cmd.add_cmd(cmd_item[0], cmd_item[1], cmd_item[2], 1)
                    self.show_status_signal.emit("导入成功： " + cmd_item[0] + ":" + cmd_item[2])
                except Exception as e:
                    self.show_status_signal.emit("导入异常： " + str(cmd_item) + str(e))
