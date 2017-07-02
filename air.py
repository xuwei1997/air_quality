import serial
import requests
import json
import time
import re

ser = serial.Serial('/dev/ttyACM1',9600,timeout=1)
key='a'
key = key.encode("ascii")

data_arr=[]
while len(data_arr)<11 :
    ser.write(key)
    da=ser.readline()
    time.sleep(0.5)
    data=re.split(r'\|' , str(da))
    if len(data)==8:
        c= int(data[2])+int(data[3])+int(data[4])
        if data[1] == 'aaa' and data[6] == 'bbb' and c== int(data[5]):
            print("a")
            data_arr.append(data)
print(data_arr)

#url='http://api.heclouds.com/devices/9106291/datapoints?type=3'
#headers = {'api-key': 'EazpwgBmpqo=S4Uhl=BOgGyWQqY='}
#payload = {'PM1_0': data[5],'PM2_5':data[6],'PM10':data[7]}
#print(payload)
#r = requests.post(url, headers=headers, data=json.dumps(payload))
#print(r)