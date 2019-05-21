'''
Created on 2019年5月20日

@author: bkd
'''
from PyQt5.Qt import QListWidgetItem

'''
Created on 2019年5月9日

@author: bkd
'''
import sys
import time
from os import environ,startfile,system
from os.path import expanduser,join
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QApplication,QDialog, \
    QMainWindow, QInputDialog,QLineEdit, QTreeWidgetItem
    
from .kdCarCheckDevSimulator_ui import Ui_MainWindow
from .fileutil import check_and_create
from .exception_handler import global_exception_hander
from . import line
from . import device
from . import cmd 

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
        self.selected_device = None
        self.selected_lineId = None
        
        self.tw_device.itemPressed.connect(self.on_tw_device_itemPressed)
        self.dlg_cmd = cmd.cmd()
        
        
                  
    def init_tw_dev(self):
        self.tw_device.clear()
        line_list = line.get_all()
        if line_list:
            for item in line_list :
                root_item = self.tw_device.invisibleRootItem()
                child = QTreeWidgetItem()
                child.setText(0, item[1])
                child.setData(0,-1,0)
                # 设置LineId
                child.setData(0,-2,item[0])
                root_item.setExpanded(True)
                child.setFlags(child.flags())
                root_item.addChild(child)
                
                device_list = device.get_all(item[0])
                if device_list:
                    for device_item in device_list:
                            dev_child = QTreeWidgetItem()
                            dev_child.setText(0, device_item[2])
                            dev_child.setData(0,-1,1)
                            # 设置device_item
                            dev_child.setData(0,-2,device_item)
                            dev_child.setFlags(child.flags())             
                            child.setExpanded(True)
                            child.addChild(dev_child)
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
            self.statusbar.showMessage("新增检测线成功")
#             QMessageBox.information(self, "检测线管理", "新增检测线成功")

    @pyqtSlot()
    def on_pb_del_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 0 :
            line_name = seleted_item.text(0)
            line.delete_line(line_name)
            
            root_item = self.tw_device.invisibleRootItem()
            root_item.removeChild(seleted_item)
            self.statusbar.showMessage("删除检测线成功")
#             QMessageBox.information(self, "检测线管理", "删除检测线成功")
   
    @pyqtSlot()
    def on_pb_modify_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 0 :
            new_line_name,ok = QInputDialog.getText(self  , "修改检测线", "检测线名称",QLineEdit.Normal,seleted_item.text(0))
            if ok :
                lineId = seleted_item.data(0,-2)
                line.modify_line(lineId,new_line_name )
                
                seleted_item.setText(0, new_line_name)
                self.statusbar.showMessage("修改检测线成功")
#             QMessageBox.information(self, "检测线管理", "修改检测线成功")
    
    @pyqtSlot()
    def on_tw_device_itemPressed(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 0 :
            self.selected_lineId = seleted_item.data(0,-2)
            self.selected_device = None
            self.on_pb_add_device_clicked()
        else :
            self.selected_device = seleted_item.data(0,-2)
            self.selected_lineId = self.selected_device[4]
            print(self.selected_device[4])
            self.le_big_item.setText(self.selected_device[1])
            self.le_dev_model.setText(self.selected_device[2])
            self.le_com_port.setText(self.selected_device[3])
            
            self.refresh_cmd()
            

#     新增设备
    @pyqtSlot()
    def on_pb_add_device_clicked(self):
        self.le_big_item.clear()
        self.le_dev_model.clear()
        self.le_com_port.clear()
        self.selected_device = None
    
#     修改设备
    @pyqtSlot()
    def on_pb_save_device_clicked(self):
        if self.selected_device :
            device.modify_device(self.le_big_item.text(), self.le_dev_model.text(), self.le_com_port.text(), self.selected_device[0]);
            self.init_tw_dev()
            self.statusbar.showMessage("更新设备成功")
        else :
            device.add_device(self.le_big_item.text(), self.le_dev_model.text(), self.le_com_port.text(), self.selected_lineId)
            self.init_tw_dev()
            self.statusbar.showMessage("新增设备成功")
#     删除设备
    @pyqtSlot()
    def on_pb_del_device_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0,-1) == 1 :
            device.delete_device(self.selected_device[0])
            self.init_tw_dev()
            self.on_pb_add_device_clicked()
            self.statusbar.showMessage("删除设备成功")
            
# 新增命令            
    @pyqtSlot()
    def on_pb_add_cmd_clicked(self):
            self.dlg_cmd.set_model(self.selected_device[2])
            self.dlg_cmd.show()
            self.dlg_cmd.add_signal.connect(self.refresh_cmd)
            self.dlg_cmd.modify_signal.connect(self.refresh_cmd)
    
    def refresh_cmd(self):
        self.lw_cmd.clear()
        cmd_list = self.dlg_cmd.get_all(self.selected_device[2])
        if cmd_list:
            for cmd_item in cmd_list :
                item =QListWidgetItem(cmd_item[3])  
                item.setData(-1,cmd_item)
                self.lw_cmd.addItem(item) 

#     删除命令
    @pyqtSlot()
    def on_pb_del_cmd_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        self.dlg_cmd.delete_cmd(seleted_item.data(-1)[0])
        
        self.refresh_cmd()
        self.statusbar.showMessage("删除命令成功")   

#     修改命令
    @pyqtSlot()
    def on_pb_modify_cmd_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        if seleted_item :
            self.dlg_cmd.set_cmd_item(seleted_item.data(-1))
            self.dlg_cmd.show()
            
            
def main():
    app = QApplication(sys.argv)
    win = kdCarCheckDevSimulator()
    win.show()
    sys.exit(app.exec_())       