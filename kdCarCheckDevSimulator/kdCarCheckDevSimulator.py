'''
Created on 2019年5月20日

@author: bkd
'''

'''
Created on 2019年5月9日

@author: bkd
'''
import sys
import time
from os import environ,startfile,system
from os.path import expanduser,join
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QApplication,QFileDialog, \
    QMainWindow, QInputDialog,QLineEdit, QMessageBox,QTreeWidgetItem
    
from .kdCarCheckDevSimulator_ui import Ui_MainWindow
from .fileutil import check_and_create
from .exception_handler import global_exception_hander
from . import line

class kdCarCheckDevSimulator(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.exception_handler = global_exception_hander()
        self.exception_handler.patch_excepthook()
        
#         self.config_file =join(expanduser('~') , ".config/kdTimer/profile.dat")
#         check_and_create(self.config_file)
        self.last_dir = None
        
        self.init_tw_dev()
        
                  
    def init_tw_dev(self):
        line_list = line.get_all()
        if line_list:
            for item in line_list :
                root_item = self.tw_device.invisibleRootItem()
                child = QTreeWidgetItem()
                child.setText(0, item[1])
                child.setData(0,-1,0)
                # 设置LineId
                child.setData(0,-2,item[0])
                root_item.addChild(child)
                root_item.setExpanded(True)
                child.setFlags(child.flags())                  
    #             获取上一次打开的目录
    def get_last_dir(self):
        if self.last_dir :
            return self.last_dir
        else :
            return expanduser("~")
        
    @pyqtSlot()
    def on_action_start_all_port_triggered(self):
        print("g")
    
    @pyqtSlot()
    def on_pb_add_line_clicked(self):
        line_name,ok = QInputDialog.getText(self  , "新增检测线", "检测线名称")
        print(ok,line_name)
        if ok :
            line.add_line(line_name)
            root_item = self.tw_device.invisibleRootItem()
            child = QTreeWidgetItem()
            child.setText(0, line_name)
            child.setData(0,-1,0)
            root_item.addChild(child)
            root_item.setExpanded(True)
            child.setFlags(child.flags())
#             QMessageBox.information(self, "检测线管理", "新增检测线成功")

    @pyqtSlot()
    def on_pb_del_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 0 :
            line_name = seleted_item.text(0)
            line.delete_line(line_name)
            
            root_item = self.tw_device.invisibleRootItem()
            root_item.removeChild(seleted_item)
#             QMessageBox.information(self, "检测线管理", "删除检测线成功")
   
    @pyqtSlot()
    def on_pb_modify_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 0 :
            new_line_name,ok = QInputDialog.getText(self  , "新增检测线", "检测线名称",QLineEdit.Normal,seleted_item.text(0))
            if ok :
                lineId = seleted_item.data(0,-2)
                line.modify_line(lineId,new_line_name )
                
                seleted_item.setText(0, new_line_name)
#             QMessageBox.information(self, "检测线管理", "修改检测线成功")

    
        
def main():
    app = QApplication(sys.argv)
    win = kdCarCheckDevSimulator()
    win.show()
    sys.exit(app.exec_())       