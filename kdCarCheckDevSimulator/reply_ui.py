# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdCarCheckDevSimulator\kdCarCheckDevSimulator\reply.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_reply(object):
    def setupUi(self, dlg_reply):
        dlg_reply.setObjectName("dlg_reply")
        dlg_reply.resize(416, 185)
        self.formLayout = QtWidgets.QFormLayout(dlg_reply)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(dlg_reply)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lb_cmd = QtWidgets.QLabel(dlg_reply)
        self.lb_cmd.setObjectName("lb_cmd")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lb_cmd)
        self.label_2 = QtWidgets.QLabel(dlg_reply)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_value = QtWidgets.QLineEdit(dlg_reply)
        self.le_value.setObjectName("le_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_value)
        self.label_3 = QtWidgets.QLabel(dlg_reply)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_remark = QtWidgets.QLineEdit(dlg_reply)
        self.le_remark.setObjectName("le_remark")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_remark)
        self.label_4 = QtWidgets.QLabel(dlg_reply)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_reply)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.sp_sequence = QtWidgets.QSpinBox(dlg_reply)
        self.sp_sequence.setObjectName("sp_sequence")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sp_sequence)

        self.retranslateUi(dlg_reply)
        QtCore.QMetaObject.connectSlotsByName(dlg_reply)

    def retranslateUi(self, dlg_reply):
        _translate = QtCore.QCoreApplication.translate
        dlg_reply.setWindowTitle(_translate("dlg_reply", "响应管理"))
        self.label.setText(_translate("dlg_reply", "命令"))
        self.lb_cmd.setText(_translate("dlg_reply", "-"))
        self.label_2.setText(_translate("dlg_reply", "16进制响应值"))
        self.label_3.setText(_translate("dlg_reply", "响应备注"))
        self.label_4.setText(_translate("dlg_reply", "响应顺序"))

