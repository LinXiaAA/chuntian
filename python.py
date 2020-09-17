# -*- coding: utf-8 -*-
import serial
import struct
import requests

url = ""

def pushup(loadup):
     try:
        re = requests.get(url, data = loadup)
        r.raise_for_status()
        return re.text
    except:
        return "HTTP ERROR"
if __name__ == "_main_":
    arduino = serial.Serial('/dev/ttyUSB0', 57600, timeout=.1)
    while True:
        if arduino.readline() == b'DUANWEIMING\n':
            data = arduino.read(12)
            bpm, IR_signalSize, xy, time = struct.unpack("<hhfL", data)
            data = {"bpm":bpm, "ir":IR_signalSize, "xy":xy, "time":time}
            pushup(data)
            print("bpm:"+bpm+"\nir:"+IR_signalSize+"\n血氧:"+xy+"\n时间:"+time)
