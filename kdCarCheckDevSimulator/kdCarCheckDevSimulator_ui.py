# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdCarCheckDevSimulator\kdCarCheckDevSimulator\kdCarCheckDevSimulator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_add_line = QtWidgets.QPushButton(self.groupBox)
        self.pb_add_line.setObjectName("pb_add_line")
        self.horizontalLayout.addWidget(self.pb_add_line)
        self.pb_del_line = QtWidgets.QPushButton(self.groupBox)
        self.pb_del_line.setObjectName("pb_del_line")
        self.horizontalLayout.addWidget(self.pb_del_line)
        self.pb_modify_line = QtWidgets.QPushButton(self.groupBox)
        self.pb_modify_line.setObjectName("pb_modify_line")
        self.horizontalLayout.addWidget(self.pb_modify_line)
        self.pb_add_device = QtWidgets.QPushButton(self.groupBox)
        self.pb_add_device.setObjectName("pb_add_device")
        self.horizontalLayout.addWidget(self.pb_add_device)
        self.pb_del_device = QtWidgets.QPushButton(self.groupBox)
        self.pb_del_device.setObjectName("pb_del_device")
        self.horizontalLayout.addWidget(self.pb_del_device)
        self.pb_save_device = QtWidgets.QPushButton(self.groupBox)
        self.pb_save_device.setObjectName("pb_save_device")
        self.horizontalLayout.addWidget(self.pb_save_device)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tw_device = QtWidgets.QTreeWidget(self.groupBox)
        self.tw_device.setObjectName("tw_device")
        self.tw_device.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.tw_device)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.le_big_item = QtWidgets.QLineEdit(self.groupBox)
        self.le_big_item.setObjectName("le_big_item")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_big_item)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.le_dev_model = QtWidgets.QLineEdit(self.groupBox)
        self.le_dev_model.setObjectName("le_dev_model")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_dev_model)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_com_port = QtWidgets.QLineEdit(self.groupBox)
        self.le_com_port.setObjectName("le_com_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_com_port)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tb_monitor = QtWidgets.QTextBrowser(self.groupBox)
        self.tb_monitor.setObjectName("tb_monitor")
        self.verticalLayout.addWidget(self.tb_monitor)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_add_cmd = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_add_cmd.setObjectName("pb_add_cmd")
        self.horizontalLayout_2.addWidget(self.pb_add_cmd)
        self.pb_del_cmd = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_del_cmd.setObjectName("pb_del_cmd")
        self.horizontalLayout_2.addWidget(self.pb_del_cmd)
        self.pb_modify_cmd = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_modify_cmd.setObjectName("pb_modify_cmd")
        self.horizontalLayout_2.addWidget(self.pb_modify_cmd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lw_cmd = QtWidgets.QListWidget(self.groupBox_2)
        self.lw_cmd.setObjectName("lw_cmd")
        self.verticalLayout_2.addWidget(self.lw_cmd)
        self.pb_connect_status = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_connect_status.setObjectName("pb_connect_status")
        self.verticalLayout_2.addWidget(self.pb_connect_status)
        self.cb_status = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_status.setObjectName("cb_status")
        self.verticalLayout_2.addWidget(self.cb_status)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pb_add_reply = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_add_reply.setObjectName("pb_add_reply")
        self.horizontalLayout_3.addWidget(self.pb_add_reply)
        self.pb_del_reply = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_del_reply.setObjectName("pb_del_reply")
        self.horizontalLayout_3.addWidget(self.pb_del_reply)
        self.pb_modify_reply = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_modify_reply.setObjectName("pb_modify_reply")
        self.horizontalLayout_3.addWidget(self.pb_modify_reply)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tw_reply = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_reply.setRowCount(10)
        self.tw_reply.setColumnCount(2)
        self.tw_reply.setObjectName("tw_reply")
        self.verticalLayout_3.addWidget(self.tw_reply)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_start_line = QtWidgets.QAction(MainWindow)
        self.action_start_line.setObjectName("action_start_line")
        self.action_stop_line = QtWidgets.QAction(MainWindow)
        self.action_stop_line.setObjectName("action_stop_line")
        self.action_start_single_dev = QtWidgets.QAction(MainWindow)
        self.action_start_single_dev.setObjectName("action_start_single_dev")
        self.action_stop_single_dev = QtWidgets.QAction(MainWindow)
        self.action_stop_single_dev.setObjectName("action_stop_single_dev")
        self.action_import_cmd_by_mysql = QtWidgets.QAction(MainWindow)
        self.action_import_cmd_by_mysql.setObjectName("action_import_cmd_by_mysql")
        self.action_import_reply_by_mysql = QtWidgets.QAction(MainWindow)
        self.action_import_reply_by_mysql.setObjectName("action_import_reply_by_mysql")
        self.toolBar.addAction(self.action_start_line)
        self.toolBar.addAction(self.action_stop_line)
        self.toolBar.addAction(self.action_start_single_dev)
        self.toolBar.addAction(self.action_stop_single_dev)
        self.toolBar.addAction(self.action_import_cmd_by_mysql)
        self.toolBar.addAction(self.action_import_reply_by_mysql)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "检测线模拟器"))
        self.groupBox.setTitle(_translate("MainWindow", "设备连接信息"))
        self.pb_add_line.setText(_translate("MainWindow", "新增检测线"))
        self.pb_del_line.setText(_translate("MainWindow", "删除检测线"))
        self.pb_modify_line.setText(_translate("MainWindow", "修改检测线"))
        self.pb_add_device.setText(_translate("MainWindow", "新增设备"))
        self.pb_del_device.setText(_translate("MainWindow", "删除设备"))
        self.pb_save_device.setText(_translate("MainWindow", "保存设备"))
        self.label_9.setText(_translate("MainWindow", "检测项目"))
        self.label_10.setText(_translate("MainWindow", "设备型号"))
        self.label_3.setText(_translate("MainWindow", "端口："))
        self.label_4.setText(_translate("MainWindow", "波特率："))
        self.label_5.setText(_translate("MainWindow", "数据位："))
        self.label_6.setText(_translate("MainWindow", "停止位："))
        self.groupBox_2.setTitle(_translate("MainWindow", "命令"))
        self.pb_add_cmd.setText(_translate("MainWindow", "新增命令"))
        self.pb_del_cmd.setText(_translate("MainWindow", "删除命令"))
        self.pb_modify_cmd.setText(_translate("MainWindow", "修改命令"))
        self.pb_connect_status.setText(_translate("MainWindow", "关联状态"))
        self.groupBox_3.setTitle(_translate("MainWindow", "响应"))
        self.pb_add_reply.setText(_translate("MainWindow", "新增响应"))
        self.pb_del_reply.setText(_translate("MainWindow", "删除响应"))
        self.pb_modify_reply.setText(_translate("MainWindow", "修改相应"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_start_line.setText(_translate("MainWindow", "启动检测线"))
        self.action_stop_line.setText(_translate("MainWindow", "停止检测线"))
        self.action_start_single_dev.setText(_translate("MainWindow", "启动单个设备"))
        self.action_stop_single_dev.setText(_translate("MainWindow", "停止单个设备"))
        self.action_import_cmd_by_mysql.setText(_translate("MainWindow", "从mysql批量导入命令"))
        self.action_import_reply_by_mysql.setText(_translate("MainWindow", "从mysql批量导入状态"))

