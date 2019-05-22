'''
Created on 2019年5月21日

@author: bkd
'''
import sqlite3
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from .cmd_ui import Ui_dlg_cmd

class cmd(QDialog,Ui_dlg_cmd):
    add_signal = pyqtSignal(str) 
    modify_signal = pyqtSignal(str) 
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_file = "data/kdCarCheckDevSimulator.db"
        self.id = None
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        if self.lb_model.text() == "-":
            return
        reply_type = 1
        if self.rb_random.isChecked:
            reply_type = 2
        
        if self.id:    
            self.modify_cmd()
            self.modify_signal.emit(self.le_remark.text())
        else :
            self.add_cmd(self.lb_model.text(), self.le_value.text().strip().upper(), self.le_remark.text().strip().upper(),reply_type)
            self.add_signal.emit(self.le_remark.text())
        self.hide()
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.hide()
        
    
    def reset(self):
        self.le_value.clear()
        self.le_remark.clear()
        
    def set_model(self,model):
        self.lb_model.setText(model)
        
    def set_cmd_item(self,item):
        self.id = item[0]
        self.lb_model.setText(item[1])
        self.le_value.setText(item[2])
        self.le_remark.setText(item[3])
        if item[4] == 1:
            self.rb_all.setChecked(True)
        else :
            self.rb_random.setChecked(True)
        
        
    def add_cmd(self, model,value,remark,reply_type):
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        cs.execute("insert into cmd (model,value,remark,reply_type) values(?,?,?,?)",(model,value,remark, reply_type))
        conn.commit()
        
    def delete_cmd(self, cmdId):
        self.run_sql("delete from cmd where id = '{}'".format(cmdId))
    def get_all(self, model):
        return self.run_sql("select id,model,value,remark,reply_type from cmd where model ='{}' order by remark".format(model))
    def modify_cmd(self):
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