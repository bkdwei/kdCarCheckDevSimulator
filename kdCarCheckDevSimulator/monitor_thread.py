# coding=utf-8
import requests
import os
from . import fileutil
import re
import time
import json
import sys
import serial
import binascii,re
from PyQt5.QtCore import QThread, pyqtSignal
from .reply import reply

class monitor_thread(QThread):
    """ 下载心情随笔的线程 """

    show_status_signal = pyqtSignal(str)

    def __init__(self,port,model,cmd_list):
        super().__init__()
        self.port = port
        self.model = model
        self.cmd_list = [c[2] for c in cmd_list]
        self.state = False 
        self.reply = reply()

   

    def run(self):
        if not self.port :
            return
               
        print(self.port)
        self.com = serial.Serial(self.port, 9600)
        if not self.com.isOpen():
            self.com.open()
            
        self.state = True
        self.receiveData()
        
#     监听数据线程
    def receiveData(self):
        try:
            while self.state:
                count = self.com.in_waiting
                if count > 0:
                    data = self.com.read(count)
                    if data and data != b'88':
                        receive_data = self.asciiB2HexString(data).strip()
                        print("receive:", receive_data)
                        if receive_data in self.cmd_list :
                            reply_list = self.reply.get_all_by_cmd_value(receive_data)
                            if reply_list:
                                print("reply:", reply_list[0][0])
                                self.com.write(self.hexStringB2Hex(reply_list[0][0]))
#                     self.com.close()
#                     break
        except KeyboardInterrupt:
            if self.com != None:
                self.com.close()

#     字节数组转16进制字符串
    def asciiB2HexString(self,strB):
        strHex = binascii.b2a_hex(strB).upper()
        return re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", strHex.decode())+" "
    
#     16进制字符串转字节数组
    def hexStringB2Hex(self,hexString):
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
            print("已关闭串口" + self.port)
