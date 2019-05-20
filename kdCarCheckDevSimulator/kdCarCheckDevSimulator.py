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
    QMainWindow, QInputDialog,QLineEdit
    
from .kdCarCheckDevSimulator_ui import Ui_MainWindow
from .fileutil import check_and_create
from .exception_handler import global_exception_hander

class kdCarCheckDevSimulator(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.exception_handler = global_exception_hander()
        self.exception_handler.patch_excepthook()
        
        self.config_file =join(expanduser('~') , ".config/kdTimer/profile.dat")
        check_and_create(self.config_file)
        self.last_dir = None
        
                  
    #             获取上一次打开的目录
    def get_last_dir(self):
        if self.last_dir :
            return self.last_dir
        else :
            return expanduser("~")
        
    @pyqtSlot()
    def on_action_start_all_port_triggered(self):
        print("g")
    
        
def main():
    app = QApplication(sys.argv)
    win = kdCarCheckDevSimulator()
    win.show()
    sys.exit(app.exec_())       