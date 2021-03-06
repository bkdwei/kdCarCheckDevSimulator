'''
Created on 2019年5月21日

@author: bkd
'''
from os.path import expanduser,join
import sqlite3
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from .reply_ui import Ui_dlg_reply

class reply(QDialog,Ui_dlg_reply):
    modify_signal = pyqtSignal() 
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_file = join(expanduser("~"),".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db")
        self.id = None
        self.cmd_id = None
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        if self.lb_cmd.text() == "-":
            return
        
        if self.id:    
            self.modify_reply()
            self.modify_signal.emit()
        else :
            self.add_reply(self.le_value.text(), self.le_remark.text(),self.sp_sequence.text(),self.cmd_id)
            self.modify_signal.emit()
        self.hide()
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.hide()
        
    def set_data(self,item,cmd):
        self.id = item[0]
        if cmd:
            self.lb_cmd.setText(cmd)
        self.le_value.setText(item[1])
        self.le_remark.setText(item[2])
        self.sp_sequence.setValue(int(item[3]))
        self.cmd_id = item[4]
        
        pass
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
        
        
    def add_reply(self, value,remark,sequence,cmd_id,model= None):
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        cs.execute("insert into reply (value,remark,sequence,cmd_id,model) values(?,?,?,?,?)",(value,remark,sequence,cmd_id,model))
        conn.commit()
        
    def delete_reply(self, replyId):
        self.run_sql("delete from reply where id = '{}'".format(replyId))
    def delete_reply_by_cmdId(self, cmdId):
        self.run_sql("delete from reply where cmd_id = '{}'".format(cmdId))
    def get_all(self, cmd_id):
        return self.run_sql("select id,value,remark,sequence,cmd_id,model from reply where cmd_id ='{}' order by sequence".format(cmd_id))
    def get_all_by_cmd_value(self, cmd_value):
        return self.run_sql("select r.value,r.remark from reply r join cmd c on r.cmd_id = c.id where c.value ='{}' order by sequence".format(cmd_value))
    def get_all_by_model(self, model):
        return self.run_sql("select id,value,remark,sequence,cmd_id, model from reply where model ='{}' order by sequence".format(model))
    def modify_reply(self):
        self.run_sql("update reply set  value ='{}', remark='{}', sequence ='{}' ,cmd_id ='{}'  ,model ='{}' where id='{}'".format(self.le_value.text().strip(),self.le_remark.text().strip(),self.sp_sequence.value(),self.cmd_id,None,self.id))
    
    def run_sql(self, sql):    
        conn = sqlite3.connect(self.db_file)
        cs = conn.cursor()
        print("execute sql:" + sql )
        cs.execute(sql)
        if "select" in sql:
            return cs.fetchall()  
        conn.commit()