'''
Created on 2019年5月21日

@author: bkd
'''
import sqlite3
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from .reply_ui import Ui_dlg_reply

class reply(QDialog,Ui_dlg_reply):
    add_signal = pyqtSignal(str) 
    modify_signal = pyqtSignal(str) 
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_file = "data/kdCarCheckDevSimulator.db"
        self.id = None
        self.cmd_id = None
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        if self.lb_cmd.text() == "-":
            return
        
        if self.id:    
            self.modify_reply()
            self.modify_signal.emit(self.le_remark.text())
        else :
            self.add_reply(self.le_value.text(), self.le_remark.text(),self.sp_sequence.text(),self.cmd_id)
            self.add_signal.emit(self.le_remark.text())
        self.hide()
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.hide()
        
    
    def set_cmd(self,cmd):
        self.lb_cmd.setText(cmd)
        
    def set_cmd_item(self,item):
        self.id = item[0]
        self.lb_cmd.setText(item[1])
        self.le_value.setText(item[2])
        self.le_remark.setText(item[3])
        if item[4] == 1:
            self.rb_all.setChecked(True)
        else :
            self.rb_random.setChecked(True)
        
        
    def add_reply(self, value,remark,sequence,cmd_id):
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        cs.execute("insert into reply (value,remark,sequence,cmd_id) values(?,?,?,?)",(value,remark,sequence,cmd_id))
        conn.commit()
        
    def delete_reply(self, cmdId):
        self.run_sql("delete from cmd where id = '{}'".format(cmdId))
    def get_all(self, model):
        return self.run_sql("select id,model,value,remark,reply_type from cmd where model ='{}'".format(model))
    def modify_reply(self):
        reply_type = 1
        if self.rb_random.isChecked():
            reply_type = 2
        self.run_sql("update cmd set  value ='{}', remark='{}', reply_type ='{}' where id='{}'".format(self.le_value.text(),self.le_remark.text(),reply_type,self.id))
    
    def run_sql(self, sql):    
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        print("execute sql:" + sql )
        cs.execute(sql)
        if "select" in sql:
            return cs.fetchall()  
        conn.commit()