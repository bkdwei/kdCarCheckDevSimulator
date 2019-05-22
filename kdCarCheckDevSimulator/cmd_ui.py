# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdCarCheckDevSimulator\kdCarCheckDevSimulator\cmd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_cmd(object):
    def setupUi(self, dlg_cmd):
        dlg_cmd.setObjectName("dlg_cmd")
        dlg_cmd.resize(416, 185)
        self.formLayout = QtWidgets.QFormLayout(dlg_cmd)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(dlg_cmd)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lb_model = QtWidgets.QLabel(dlg_cmd)
        self.lb_model.setObjectName("lb_model")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lb_model)
        self.le_value = QtWidgets.QLineEdit(dlg_cmd)
        self.le_value.setObjectName("le_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_value)
        self.le_remark = QtWidgets.QLineEdit(dlg_cmd)
        self.le_remark.setObjectName("le_remark")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_remark)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_cmd)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.label_3 = QtWidgets.QLabel(dlg_cmd)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(dlg_cmd)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rb_random = QtWidgets.QRadioButton(dlg_cmd)
        self.rb_random.setObjectName("rb_random")
        self.buttonGroup = QtWidgets.QButtonGroup(dlg_cmd)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_random)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rb_random)
        self.rb_all = QtWidgets.QRadioButton(dlg_cmd)
        self.rb_all.setChecked(True)
        self.rb_all.setObjectName("rb_all")
        self.buttonGroup.addButton(self.rb_all)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rb_all)
        self.label_4 = QtWidgets.QLabel(dlg_cmd)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(dlg_cmd)
        QtCore.QMetaObject.connectSlotsByName(dlg_cmd)

    def retranslateUi(self, dlg_cmd):
        _translate = QtCore.QCoreApplication.translate
        dlg_cmd.setWindowTitle(_translate("dlg_cmd", "命令管理"))
        self.label.setText(_translate("dlg_cmd", "设备型号"))
        self.lb_model.setText(_translate("dlg_cmd", "-"))
        self.label_3.setText(_translate("dlg_cmd", "命令备注"))
        self.label_2.setText(_translate("dlg_cmd", "16进制命令值"))
        self.rb_random.setText(_translate("dlg_cmd", "随机响应一个"))
        self.rb_all.setText(_translate("dlg_cmd", "全部响应"))
        self.label_4.setText(_translate("dlg_cmd", "响应方式"))

