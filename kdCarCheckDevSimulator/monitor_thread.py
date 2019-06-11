# coding=utf-8
import binascii
import random
from re import sub
import time

from PyQt5.QtCore import QThread, pyqtSignal
import serial

from .reply import reply


class monitor_thread(QThread):

    show_status_signal = pyqtSignal(str)

    def __init__(self, port, model, cmd_list, com=None):
        super().__init__()
        self.port = port
        self.model = model
        self.cmd_list = [c[2].upper() for c in cmd_list]
        self.cmd_reply_type = {c[2]: c[4] for c in cmd_list}  # 记录命令的响应方式
        print(self.cmd_reply_type)
        self.state = False
        self.reply = reply()
        self.reply_index = {}  # 缓存指定的类型为全部响应的命令的响应列表的位置

        # 修正两个项目共用一个设备，导致无法打开串口的bug
        self.com = com

    def run(self):
        try:
            if not self.port:
                return
    
            print("启动设备：" + self.model + ",串口：" + self.port)
            self.show_status_signal.emit(
                "启动设备：" + self.model + ",串口：" + self.port)
            if not self.com:
                self.com = serial.Serial(self.port, 9600, parity='N', stopbits=1, timeout=1)
            if not self.com.isOpen():
                self.com.open()
    
            self.state = True
            self.receiveData()
        except Exception as e:
            self.show_status_signal.emit(
                "线程异常：" + self.model + ",串口：" + self.port + ",异常详情:" + str(e))

#     监听数据线程
    def receiveData(self):
        try:
            while self.state:
                count = self.com.in_waiting
                if count > 0:
                    data = self.com.read(count)
                    if data:
                        receive_data = self.asciiB2HexString(data).strip().upper()
                        now = time.strftime(
                            '[%Y:%m:%d:%H:%M:%S]', time.localtime(time.time()))
                        print(now + "receive:", receive_data)
                        self.show_status_signal.emit(
                            self.model + "," + now + "[接收]" + receive_data)
                       
                        if not receive_data in self.cmd_list:
                            continue
                        
                        # 获取响应类型
                        if not self.cmd_reply_type :
                            continue
                        print("aa")
                        reply_type = self.cmd_reply_type[receive_data]
                        if reply_type == 1:
                            reply_list = self.reply.get_all_by_cmd_value(receive_data)
                            if not reply_list :
                                continue
                            
                            index = 0
                            print("ab")
                            if receive_data in self.reply_index.keys() :
                                index = int(self.reply_index[receive_data]) + 1
                                # 判断是否越界
                                if index >= len(reply_list):
                                    index = 0
                            self.reply_index[receive_data] = index
                            
                            print(index, len(reply_list))
                            
                            reply_item = reply_list[index]
                            print("reply:", reply_item[1], reply_item[0])
                            send_msg = self.hexStringB2Hex(reply_item[0])
                            self.com.write(send_msg)
                            now = time.strftime(
                                '[%Y:%m:%d:%H:%M:%S]', time.localtime(time.time()))
                            self.show_status_signal.emit(
                                self.model + "," + now + "[发送]" + reply_item[0] + "  -  " + reply_item[1])
                            #time.sleep(1)
                        else:
                            reply_list = self.reply.get_all_by_cmd_value(receive_data)

                            if len(reply_list) == 0:
                                continue
                            index = random.randint(-1,
                                                   len(reply_list) - 1)
                            print("index:" + str(index))
                            print(
                                "reply:", reply_list[index][0])
                            send_msg = self.hexStringB2Hex(
                                reply_list[index][0])
                            self.com.write(send_msg)
                            self.show_status_signal.emit(
                                self.model + "," + now + "[发送]" + reply_list[index][0] + "  -  " + reply_list[index][1])
        except KeyboardInterrupt:
            pass

#     字节数组转16进制字符串
    def asciiB2HexString(self, strB):
        strHex = binascii.b2a_hex(strB).upper()
        return sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", strHex.decode()) + " "

#     16进制字符串转字节数组
    def hexStringB2Hex(self, hexString):
        dataList = hexString.split(" ")
        j = 0
        for i in dataList:
            if len(i) > 2:
                return -1
            elif len(i) == 1:
                dataList[j] = "0" + i
            j += 1
        data = "".join(dataList)
        try:
            data = bytes.fromhex(data)
        except Exception:
            return -1
        # print(data)
        return data

    def stop(self):
        if self.state:
            self.state = False
            self.show_status_signal.emit(self.model + ",已关闭串口:" + self.port)
            print("已关闭串口" + self.port)

    # 直接发送响应
    def send(self, msg):
        send_msg = self.hexStringB2Hex(msg)
        self.com.write(send_msg)
        now = time.strftime(
            '[%Y:%m:%d:%H:%M:%S]', time.localtime(time.time()))
        self.show_status_signal.emit(
            self.model + "," + now + "[直接发送]" + msg)
