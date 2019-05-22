'''
Created on 2019年5月22日

@author: bkd
'''
import MySQLdb

from .reply import reply

from PyQt5.QtCore import QThread, pyqtSignal

class import_reply(QThread):
    show_status_signal = pyqtSignal(str)
    def __init__(self,connect_str):
        super().__init__()
        self.connect_str = connect_str
        
        
        
    def run(self):
        dlg_reply = reply()
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
        cursor.execute("SELECT m.model,s.status_value,s.cn_name from dev_status s join  dev_model m on s.model_id = m.id where s.del_flag = '0' order by m.model")
        
        # 使用 fetchone() 方法获取一条数据
        reply_list = cursor.fetchall()
        
        # 关闭数据库连接
        db.close()
        if reply_list :
            print(reply_list)
            for reply_item in reply_list :
                try:
                    dlg_reply.add_reply(reply_item[1], reply_item[2],1,None, reply_item[0])
                    self.show_status_signal.emit("导入成功： " + reply_item[0] + ":" + reply_item[2])
                except Exception as e:
                    self.show_status_signal.emit("导入异常： " + str(reply_item) + str(e))
