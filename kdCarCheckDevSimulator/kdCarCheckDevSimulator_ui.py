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
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 150, 181, 411))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 54, 12))
        self.label.setObjectName("label")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 50, 181, 71))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 130, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 170, 54, 12))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(340, 80, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(340, 130, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(350, 170, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(230, 280, 256, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 250, 54, 12))
        self.label_7.setObjectName("label_7")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(510, 280, 256, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 250, 54, 12))
        self.label_8.setObjectName("label_8")
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
        self.action_start_all_dev = QtWidgets.QAction(MainWindow)
        self.action_start_all_dev.setObjectName("action_start_all_dev")
        self.action_stop_all_dev = QtWidgets.QAction(MainWindow)
        self.action_stop_all_dev.setObjectName("action_stop_all_dev")
        self.action_start_single_dev = QtWidgets.QAction(MainWindow)
        self.action_start_single_dev.setObjectName("action_start_single_dev")
        self.action_stop_single_dev = QtWidgets.QAction(MainWindow)
        self.action_stop_single_dev.setObjectName("action_stop_single_dev")
        self.toolBar.addAction(self.action_start_all_dev)
        self.toolBar.addAction(self.action_stop_all_dev)
        self.toolBar.addAction(self.action_start_single_dev)
        self.toolBar.addAction(self.action_stop_single_dev)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "检测设备"))
        self.label_2.setText(_translate("MainWindow", "检测线"))
        self.label_3.setText(_translate("MainWindow", "端口："))
        self.label_4.setText(_translate("MainWindow", "波特率："))
        self.label_5.setText(_translate("MainWindow", "数据位："))
        self.label_6.setText(_translate("MainWindow", "停止位："))
        self.label_7.setText(_translate("MainWindow", "命令"))
        self.label_8.setText(_translate("MainWindow", "响应"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_start_all_dev.setText(_translate("MainWindow", "启动所有设备"))
        self.action_stop_all_dev.setText(_translate("MainWindow", "停止所有设备"))
        self.action_start_single_dev.setText(_translate("MainWindow", "启动单个设备"))
        self.action_stop_single_dev.setText(_translate("MainWindow", "停止单个设备"))

