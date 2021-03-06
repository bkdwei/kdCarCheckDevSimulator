'''
Created on 2019年5月20日

@author: bkd
'''
'''
Created on 2019年5月9日

@author: bkd
'''

from os.path import expanduser, join, exists
from shutil import copy2
import sys

from PyQt5.Qt import QListWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit, QTreeWidgetItem, QTableWidgetItem

from . import cmd
from . import device
from . import line
from . import reply
from .exception_handler import global_exception_hander
from .fileutil import check_and_create_dir, get_file_realpath
from .import_cmd import import_cmd
from .import_reply import import_reply
from .kdCarCheckDevSimulator_ui import Ui_MainWindow
from .monitor_thread import monitor_thread


class kdCarCheckDevSimulator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exception_handler = global_exception_hander()
        self.exception_handler.patch_excepthook()

        self.last_dir = None
        check_and_create_dir(
            join(expanduser("~"), ".config/kdCarCheckDevSimulator"))
        if not exists(join(expanduser("~"), ".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db")):
            copy2(get_file_realpath("../data/kdCarCheckDevSimulator.db"),
                  join(expanduser("~"), ".config/kdCarCheckDevSimulator/kdCarCheckDevSimulator.db"))

        self.init_tw_dev()
        self.selected_device = None
        self.selected_lineId = None
        self.cmd_id = None
        self.cloning_device = None

        self.tw_device.itemPressed.connect(self.on_tw_device_itemPressed)
        self.tw_reply.itemClicked.connect(self.on_tw_reply_itemClicked)
        self.lw_cmd.clicked.connect(self.on_lw_cmd_clicked)
        self.dlg_cmd = cmd.cmd()
        self.dlg_reply = reply.reply()
        self.thread_list = {}
#         self.dlg_reply.add_signal.connect(self.refresh_cmd)
        self.dlg_reply.modify_signal.connect(self.refresh_reply_by_thread)

    def init_tw_dev(self):
        self.tw_device.clear()
        line_list = line.get_all()
        if line_list:
            for item in line_list:
                root_item = self.tw_device.invisibleRootItem()
                child = QTreeWidgetItem()
                child.setText(0, item[1])
                child.setData(0, -1, 0)
                # 设置LineId
                child.setData(0, -2, item[0])
                root_item.setExpanded(True)
                child.setFlags(child.flags())
                root_item.addChild(child)

                device_list = device.get_all(item[0])
                if device_list:
                    for device_item in device_list:
                        dev_child = QTreeWidgetItem()
                        dev_child.setText(
                            0, device_item[2] + "_" + device_item[1])
                        dev_child.setData(0, -1, 1)
                        # 设置device_item
                        dev_child.setData(0, -2, device_item)
                        dev_child.setFlags(child.flags())
                        child.setExpanded(True)
                        child.addChild(dev_child)
    #             获取上一次打开的目录

    def get_last_dir(self):
        if self.last_dir:
            return self.last_dir
        else:
            return expanduser("~")

    @pyqtSlot()
    def on_action_start_all_port_triggered(self):
        print("g")

#     停止单个设备
    @pyqtSlot()
    def on_action_stop_single_dev_triggered(self):
        if not self.selected_device:
            return
        # 判断是否已经关闭过这个端口
        if self.selected_device[3] in self.thread_list:
            t = self.thread_list[self.selected_device[3]]
            if t:
                t.stop()
                t.terminate()
                del self.thread_list[self.selected_device[3]]
        else:
            self.show_monitor_status(self.selected_device[3] + "已被其他线程关闭")

#     启动单个设备
    @pyqtSlot()
    def on_action_start_single_dev_triggered(self):
        if not self.selected_device:
            return
        cmd_list = self.dlg_cmd.get_all(self.selected_device[2])
        com = None
        # 判断是否已经打开过这个端口
        if self.selected_device[3] in self.thread_list:
            com = self.thread_list[self.selected_device[3]].com
        t = monitor_thread(
            self.selected_device[3], self.selected_device[2], cmd_list, com)
        t.show_status_signal.connect(self.show_monitor_status)
        self.thread_list[self.selected_device[3]] = t
        t.start()

#     启动检测线
    @pyqtSlot()
    def on_action_start_line_triggered(self):
        if not self.selected_lineId:
            self.statusbar.showMessage("请先选择检测线")
            return

        device_list = device.get_all(self.selected_lineId)
        if not device_list:
            return

        for device_item in device_list:
            cmd_list = self.dlg_cmd.get_all(device_item[2])
            com = None
            # 判断是否已经打开过这个端口
            if device_item[3] in self.thread_list:
                com = self.thread_list[device_item[3]].com
            t = monitor_thread(
                device_item[3], device_item[2], cmd_list, com)
            t.show_status_signal.connect(self.show_monitor_status)
            self.thread_list[device_item[3]] = t
            t.start()

#     停止检测线
    @pyqtSlot()
    def on_action_stop_line_triggered(self):
        if not self.selected_lineId:
            self.statusbar.showMessage("请先选择检测线")
            return
        device_list = device.get_all(self.selected_lineId)
        if not device_list:
            return

        for device_item in device_list:
            # 判断串口是否已关闭过
            if device_item[3] in self.thread_list:
                t = self.thread_list[device_item[3]]
                if t:
                    t.stop()
                    t.terminate()
                    del self.thread_list[device_item[3]]
            else:
                self.show_monitor_status(device_item[3] + "已被其他线程关闭")

#     从mysql导入命令
    @pyqtSlot()
    def on_action_import_cmd_by_mysql_triggered(self):
        connect_str, ok = QInputDialog.getText(
            self, "批量导入命令", "数据库连接信息,以分号分隔，如\nhost;port;user;password;db")
        if ok:
            self.import_cmd = import_cmd(connect_str)
            self.import_cmd.show_status_signal.connect(
                self.show_monitor_status)
            self.import_cmd.start()

#     从mysql导入状态
    @pyqtSlot()
    def on_action_import_reply_by_mysql_triggered(self):
        connect_str, ok = QInputDialog.getText(
            self, "批量导入状态", "数据库连接信息,以分号分隔，如\nhost;port;user;password;db")
        if ok:
            self.import_reply = import_reply(connect_str)
            self.import_reply.show_status_signal.connect(
                self.show_monitor_status)
            self.import_reply.start()

    def show_monitor_status(self, msg):
        self.tb_monitor.append(msg)
        self.tb_monitor.moveCursor(self.tb_monitor.textCursor().End)

    # 直接发送响应
    @pyqtSlot()
    def on_pb_direct_reply_clicked(self):
        if not self.selected_device:
            self.statusbar.showMessage("请先选择设备")
            return

        msg = self.le_direct_reply.text().strip()
        if msg == "":
            self.statusbar.showMessage("请先输入要发送的16进制内容")
            return

        if self.selected_device[3] in self.thread_list:
            t = self.thread_list[self.selected_device[3]]
            t.send(msg)

    @pyqtSlot()
    def on_pb_add_line_clicked(self):
        line_name, ok = QInputDialog.getText(self, "新增检测线", "检测线名称")
        if ok:
            line.add_line(line_name)
            root_item = self.tw_device.invisibleRootItem()
            child = QTreeWidgetItem()
            child.setText(0, line_name)
            child.setData(0, -1, 0)
            root_item.addChild(child)
            root_item.setExpanded(True)
            child.setFlags(child.flags())
            self.statusbar.showMessage("新增检测线成功")
#             QMessageBox.information(self, "检测线管理", "新增检测线成功")

    @pyqtSlot()
    def on_pb_del_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0, -1) == 0:
            line_name = seleted_item.text(0)
            line.delete_line(line_name)

            root_item = self.tw_device.invisibleRootItem()
            root_item.removeChild(seleted_item)
            self.statusbar.showMessage("删除检测线成功")
#             QMessageBox.information(self, "检测线管理", "删除检测线成功")

    @pyqtSlot()
    def on_pb_modify_line_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0, -1) == 0:
            new_line_name, ok = QInputDialog.getText(
                self, "修改检测线", "检测线名称", QLineEdit.Normal, seleted_item.text(0))
            if ok:
                lineId = seleted_item.data(0, -2)
                line.modify_line(lineId, new_line_name)

                seleted_item.setText(0, new_line_name)
                self.statusbar.showMessage("修改检测线成功")
#             QMessageBox.information(self, "检测线管理", "修改检测线成功")

    @pyqtSlot()
    def on_tw_device_itemPressed(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0, -1) == 0:
            self.selected_lineId = seleted_item.data(0, -2)
            self.selected_device = None
#             self.on_pb_add_device_clicked()
            self.tw_reply.clear()
        else:
            self.selected_device = seleted_item.data(0, -2)
#             self.selected_lineId = self.selected_device[4]
            self.selected_lineId = None
            self.le_big_item.setText(self.selected_device[1])
            self.le_dev_model.setText(self.selected_device[2])
            self.le_com_port.setText(self.selected_device[3])

            self.refresh_cmd()
            self.tw_reply.clear()

#             获取设备的相应
            reply_list = self.dlg_reply.get_all_by_model(
                self.selected_device[2])
            if reply_list:
                self.cb_status.clear()
                for reply_item in reply_list:
                    self.cb_status.addItem(reply_item[2], reply_item)

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
        if self.selected_device:
            device.modify_device(self.le_big_item.text(), self.le_dev_model.text(
            ), self.le_com_port.text(), self.selected_device[0])
            self.init_tw_dev()
            self.statusbar.showMessage("更新设备成功")
        else:
            if not self.selected_lineId:
                self.statusbar.showMessage("请选选择检测线")
                return
            device.add_device(self.le_big_item.text(), self.le_dev_model.text(
            ), self.le_com_port.text().upper(), self.selected_lineId)
            self.init_tw_dev()
            self.statusbar.showMessage("新增设备成功")
#     删除设备

    @pyqtSlot()
    def on_pb_del_device_clicked(self):
        seleted_item = self.tw_device.currentItem()
        if seleted_item.data(0, -1) == 1:
            device.delete_device(self.selected_device[0])
            self.init_tw_dev()
            self.on_pb_add_device_clicked()
            self.statusbar.showMessage("删除设备成功")

# 新增命令
    @pyqtSlot()
    def on_pb_add_cmd_clicked(self):
        if self.selected_device:
            self.dlg_cmd.set_model(self.selected_device[2])
            self.dlg_cmd.reset()
            self.dlg_cmd.show()
            self.dlg_cmd.add_signal.connect(self.refresh_cmd)
            self.dlg_cmd.modify_signal.connect(self.refresh_cmd)

    def refresh_cmd(self):
        self.lw_cmd.clear()
        cmd_list = self.dlg_cmd.get_all(self.selected_device[2])
        if cmd_list:
            for cmd_item in cmd_list:
                item = QListWidgetItem(cmd_item[3])
                item.setData(-1, cmd_item)
                self.lw_cmd.addItem(item)

#     删除命令
    @pyqtSlot()
    def on_pb_del_cmd_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        self.dlg_reply.delete_reply_by_cmdId(seleted_item.data(-1)[0])
        self.tw_reply.clear()

        self.dlg_cmd.delete_cmd(seleted_item.data(-1)[0])
        self.refresh_cmd()

        self.statusbar.showMessage("删除命令成功")

#     修改命令
    @pyqtSlot()
    def on_pb_modify_cmd_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        if seleted_item:
            self.dlg_cmd.set_cmd_item(seleted_item.data(-1))
            self.dlg_cmd.show()

#     单击命令
    @pyqtSlot()
    def on_lw_cmd_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        self.tw_reply.clear()
        if seleted_item:
            #             print(seleted_item.data(-1)[3])
            item = seleted_item.data(-1)
            self.cmd_id = item[0]
            self.refresh_reply(item[0])
            reply_type = "全部响应"
            if item[4] == 2:
                reply_type = "随机响应"
            self.statusbar.showMessage(
                item[3] + ",16进制值：" + item[2] + ",响应方式：" + reply_type)


# 新增响应
    @pyqtSlot()
    def on_pb_add_reply_clicked(self):
        seleted_item = self.lw_cmd.currentItem()
        if seleted_item:
            self.dlg_reply.set_cmd(seleted_item.data(-1)[3])
            self.dlg_reply.cmd_id = seleted_item.data(-1)[0]
            self.dlg_reply.id = None
            self.dlg_reply.show()
# 删除响应

    @pyqtSlot()
    def on_pb_del_reply_clicked(self):
        cur_row = self.tw_reply.currentRow()
        seleted_item = self.tw_reply.item(cur_row, 1)
        if seleted_item:
            item = seleted_item.data(-1)
            if item:
                self.dlg_reply.delete_reply(item[0])
                self.refresh_reply(item[4])

#     刷新响应表格
    def refresh_reply(self, cmd_id):
        reply_list = self.dlg_reply.get_all(cmd_id)
        if reply_list:
            row_index = 0
            self.tw_reply.clear()
            for reply_item in reply_list:
                print(reply_item)
                item_index = QTableWidgetItem(str(reply_item[3]))
                self.tw_reply.setItem(row_index, 0, item_index)

                item = QTableWidgetItem(reply_item[2])
                item.setData(-1, reply_item)
                self.tw_reply.setItem(row_index, 1, item)

                row_index = row_index + 1

    def refresh_reply_by_thread(self):
        self.refresh_reply(self.cmd_id)

    @pyqtSlot()
    def on_pb_connect_status_clicked(self):
        reply = self.cb_status.currentData()
        if self.cmd_id:
            self.dlg_reply.add_reply(
                reply[1], reply[2], reply[3], self.cmd_id, None)
            self.refresh_reply_by_thread()
            self.statusbar.showMessage("关联命令成功")

    @pyqtSlot()
    def on_pb_modify_reply_clicked(self):
        cur_row = self.tw_reply.currentRow()
        seleted_item = self.tw_reply.item(cur_row, 1)
        if seleted_item:
            item = seleted_item.data(-1)
            if item:
                seleted_cmd = self.lw_cmd.currentItem()
                cmd = seleted_cmd.text()
                self.dlg_reply.set_data(item, cmd)
                self.dlg_reply.show()

    def on_tw_reply_itemClicked(self):
        cur_row = self.tw_reply.currentRow()
        seleted_item = self.tw_reply.item(cur_row, 1)
        if seleted_item:
            item = seleted_item.data(-1)
            if item:
                self.statusbar.showMessage(item[2] + "，16进制值：" + item[1])

#     清空终端的消息
    @pyqtSlot()
    def on_action_clear_terminal_triggered(self):
        self.tb_monitor.clear()

#     克隆设备
    @pyqtSlot()
    def on_action_copy_device_triggered(self):
        if not self.selected_device:
            self.statusbar.showMessage("请先选择需要克隆的设备")
            return
        self.cloning_device = self.selected_device
        self.statusbar.showMessage("克隆的设备成功，请选择检测线并粘贴设备")

#     粘贴设备
    @pyqtSlot()
    def on_action_paste_device_triggered(self):
        if not self.cloning_device:
            self.statusbar.showMessage("请先克隆设备")
            return

        if not self.selected_lineId:
            self.statusbar.showMessage("请先选择需要粘贴设备的检测线")
            return
        device.add_device(
            self.cloning_device[1], self.cloning_device[2], self.cloning_device[3], self.selected_lineId)
        self.init_tw_dev()
        self.statusbar.showMessage("新增设备成功")


def main():
    app = QApplication(sys.argv)
    win = kdCarCheckDevSimulator()
    win.show()
    sys.exit(app.exec_())
